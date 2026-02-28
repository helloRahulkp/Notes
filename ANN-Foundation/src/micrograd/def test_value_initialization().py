from engine import Value
import math

def test_value_initialization():
    """Test Value initialization with default and custom parameters."""
    v = Value(5.0)
    assert v.data == 5.0
    assert v.grad == 0.0
    assert v.label == ''
    
    v_labeled = Value(3.0, label='test')
    assert v_labeled.label == 'test'


def test_addition():
    """Test addition operation and gradient computation."""
    a = Value(2.0)
    b = Value(3.0)
    c = a + b
    
    assert c.data == 5.0
    c.backward()
    assert a.grad == 1.0
    assert b.grad == 1.0


def test_addition_with_scalar():
    """Test addition with scalar values."""
    a = Value(2.0)
    c = a + 3.0
    assert c.data == 5.0
    c.backward()
    assert a.grad == 1.0


def test_multiplication():
    """Test multiplication operation and gradient computation."""
    a = Value(2.0)
    b = Value(3.0)
    c = a * b
    
    assert c.data == 6.0
    c.backward()
    assert a.grad == 3.0
    assert b.grad == 2.0


def test_subtraction():
    """Test subtraction operation."""
    a = Value(5.0)
    b = Value(3.0)
    c = a - b
    
    assert c.data == 2.0
    c.backward()
    assert a.grad == 1.0
    assert b.grad == -1.0


def test_division():
    """Test division operation."""
    a = Value(6.0)
    b = Value(2.0)
    c = a / b
    
    assert c.data == 3.0
    c.backward()
    assert a.grad == 0.5
    assert abs(b.grad - (-1.5)) < 1e-6


def test_power():
    """Test power operation."""
    a = Value(2.0)
    b = a ** 3
    
    assert b.data == 8.0
    b.backward()
    assert a.grad == 12.0


def test_negation():
    """Test negation operation."""
    a = Value(5.0)
    b = -a
    
    assert b.data == -5.0
    b.backward()
    assert a.grad == -1.0


def test_tanh():
    """Test tanh activation function."""
    a = Value(0.0)
    b = a.tanh()
    
    assert b.data == 0.0
    b.backward()
    assert a.grad == 1.0


def test_relu():
    """Test ReLU activation function."""
    a = Value(2.0)
    b = a.relu()
    assert b.data == 2.0
    b.backward()
    assert a.grad == 1.0
    
    a2 = Value(-2.0)
    b2 = a2.relu()
    assert b2.data == 0.0
    b2.backward()
    assert a2.grad == 0.0


def test_exp():
    """Test exponential function."""
    a = Value(0.0)
    b = a.exp()
    
    assert b.data == 1.0
    b.backward()
    assert b.grad == 1.0


def test_complex_graph():
    """Test backpropagation on a complex computational graph."""
    a = Value(2.0)
    b = Value(3.0)
    c = a * b + a ** 2
    d = c * b
    
    d.backward()
    assert a.grad == 16.0
    assert b.grad == 12.0


def test_chain_rule():
    """Test chain rule with nested operations."""
    a = Value(3.0)
    b = a * 2
    c = b + 1
    d = c * c
    
    d.backward()
    assert a.grad == 48.0