import math


class Value:
    """
    Core scalar Value object for automatic differentiation.
    Stores data, gradient, and graph connections.
    """

    def __init__(self, data, children=(), _op='', label=''):
        """Initialize a Value node with data and gradient tracking."""
        self.data = float(data)  # Store the scalar value
        self.grad = 0.0  # Accumulated gradient from backpropagation

        # Internal graph variables
        self._backward = lambda: None  # Function to compute gradients of parents
        self._prev = set(children)  # Previous nodes (inputs to this operation)
        self._op = _op  # Operation that produced this value (e.g., '+', '*')

        # Optional label (for graph visualization)
        self.label = label

    def __repr__(self):
        """String representation of the Value."""
        return f"Value(data={self.data}, grad={self.grad})"

    # -----------------
    # Basic Operations
    # -----------------

    def __add__(self, other):
        """Addition operation with gradient computation."""
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            # Gradient flows unchanged through addition
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad

        out._backward = _backward
        return out

    def __radd__(self, other):
        """Right addition to support Value + scalar."""
        return self + other

    def __mul__(self, other):
        """Multiplication operation with gradient computation."""
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            # Product rule: d(xy)/dx = y, d(xy)/dy = x
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward
        return out

    def __rmul__(self, other):
        """Right multiplication to support scalar * Value."""
        return self * other

    def __neg__(self):
        """Negation operation."""
        return self * -1

    def __sub__(self, other):
        """Subtraction operation (implemented via negation and addition)."""
        return self + (-other)

    def __truediv__(self, other):
        """Division operation (implemented via multiplication by reciprocal)."""
        other = other if isinstance(other, Value) else Value(other)
        return self * other**-1

    def __pow__(self, other):
        """Power operation with gradient computation."""
        assert isinstance(other, (int, float)), "Only int/float powers supported"
        out = Value(self.data**other, (self,), f'**{other}')

        def _backward():
            # Power rule: d(x^n)/dx = n * x^(n-1)
            self.grad += other * (self.data**(other-1)) * out.grad

        out._backward = _backward
        return out

    # -----------------
    # Activation Functions
    # -----------------

    def tanh(self):
        """Hyperbolic tangent activation function."""
        x = self.data
        t = (math.exp(2*x) - 1) / (math.exp(2*x) + 1)
        out = Value(t, (self,), 'tanh')

        def _backward():
            # Derivative of tanh: d(tanh(x))/dx = 1 - tanh(x)^2
            self.grad += (1 - t**2) * out.grad

        out._backward = _backward
        return out

    def relu(self):
        """Rectified Linear Unit activation function."""
        x = self.data
        out = Value(max(0, x), (self,), 'ReLU')

        def _backward():
            # ReLU derivative: 1 if x > 0, else 0
            self.grad += (1.0 if x > 0 else 0.0) * out.grad

        out._backward = _backward
        return out

    def exp(self):
        """Exponential function."""
        x = self.data
        out = Value(math.exp(x), (self,), 'exp')

        def _backward():
            # Derivative of e^x: d(e^x)/dx = e^x
            self.grad += out.data * out.grad

        out._backward = _backward
        return out

    # -----------------
    # Backpropagation
    # -----------------

    def backward(self):
        """
        Performs reverse-mode autodiff using topological ordering.
        Computes gradients of all nodes in the computational graph.
        """
        # Build topological order of computation graph
        topo = []
        visited = set()

        def build_topo(v):
            """Recursively build topological order via DFS."""
            if v not in visited:
                visited.add(v)
                # Visit all parent nodes first
                for child in v._prev:
                    build_topo(child)
                # Append after visiting children
                topo.append(v)

        build_topo(self)

        # Initialize gradient of output node
        self.grad = 1.0

        # Propagate gradients in reverse topological order
        for node in reversed(topo):
            node._backward()