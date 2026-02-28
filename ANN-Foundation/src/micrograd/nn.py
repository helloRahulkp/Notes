import random
from .engine import Value


class Neuron:
    """
    Single artificial neuron.

    Computes:
        tanh(w1*x1 + w2*x2 + ... + b)
    """

    def __init__(self, nin):
        """Initialize a neuron with random weights and bias.
        
        Args:
            nin: Number of input features
        """
        # Initialize weights randomly between -1 and 1
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]

        # Initialize bias randomly between -1 and 1
        self.b = Value(random.uniform(-1, 1))


    def __call__(self, x):
        """Forward pass: compute weighted sum and apply tanh activation.
        
        Args:
            x: Input vector of values
            
        Returns:
            Output value after tanh activation
        """
        # Compute weighted sum of inputs plus bias
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)

        # Apply tanh activation function
        out = act.tanh()

        return out


    def parameters(self):
        """Return all learnable parameters (weights and bias).
        
        Returns:
            List of all weights and bias
        """
        return self.w + [self.b]


    def __repr__(self):
        """String representation of the neuron."""
        return f"Neuron({len(self.w)} inputs)"



class Layer:
    """
    A layer of neurons.
    """

    def __init__(self, nin, nout):
        """Initialize a layer with multiple neurons.
        
        Args:
            nin: Number of input features per neuron
            nout: Number of neurons in this layer
        """
        self.neurons = [Neuron(nin) for _ in range(nout)]


    def __call__(self, x):
        """Forward pass through all neurons in the layer.
        
        Args:
            x: Input vector
            
        Returns:
            Single output if layer has 1 neuron, otherwise list of outputs
        """
        # Compute output from each neuron
        outs = [n(x) for n in self.neurons]

        # Return single value or list of values
        return outs[0] if len(outs) == 1 else outs


    def parameters(self):
        """Return all learnable parameters from all neurons.
        
        Returns:
            Flattened list of all weights and biases
        """
        return [p for neuron in self.neurons for p in neuron.parameters()]


    def __repr__(self):
        """String representation of the layer."""
        return f"Layer({len(self.neurons)} neurons)"



class MLP:
    """
    Multi-Layer Perceptron.

    Example:
        MLP(3, [4,4,1])
    """

    def __init__(self, nin, nouts):
        """Initialize a multi-layer neural network.
        
        Args:
            nin: Number of input features
            nouts: List of output sizes for each layer
        """
        # Create size list: [input_size, hidden_sizes..., output_size]
        sz = [nin] + nouts

        # Create layers with appropriate input/output dimensions
        self.layers = [
            Layer(sz[i], sz[i+1])
            for i in range(len(nouts))
        ]


    def __call__(self, x):
        """Forward pass through all layers.
        
        Args:
            x: Input vector
            
        Returns:
            Final output from the network
        """
        # Propagate input through each layer sequentially
        for layer in self.layers:
            x = layer(x)

        return x


    def parameters(self):
        """Return all learnable parameters from all layers.
        
        Returns:
            Flattened list of all weights and biases
        """
        return [p for layer in self.layers for p in layer.parameters()]


    def zero_grad(self):
        """Reset gradients of all parameters to zero."""
        for p in self.parameters():
            p.grad = 0.0


    def __repr__(self):
        """String representation showing network architecture."""
        layer_sizes = " → ".join(str(len(layer.neurons)) for layer in self.layers)

        return f"MLP({layer_sizes})"