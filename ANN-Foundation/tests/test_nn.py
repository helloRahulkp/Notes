import pytest
from micrograd.engine import Value
from micrograd.nn import Neuron, Layer, MLP

# -----------------------------
# Neuron Tests
# -----------------------------
def test_neuron_forward():
    n = Neuron(2)
    x = [Value(1.0), Value(-2.0)]
    out = n(x)
    assert isinstance(out, Value), "Neuron output should be a Value object"

def test_neuron_backward():
    n = Neuron(2)
    x = [Value(1.0), Value(-2.0)]
    out = n(x)
    out.backward()
    # gradients of weights and bias should be non-zero
    for w in n.w:
        assert w.grad != 0.0, "Weight gradient should not be zero after backward"
    assert n.b.grad != 0.0, "Bias gradient should not be zero after backward"

# -----------------------------
# Layer Tests
# -----------------------------
def test_layer_forward():
    l = Layer(3, 2)  # 3 inputs, 2 neurons
    x = [Value(1.0), Value(0.5), Value(-1.0)]
    out = l(x)
    assert isinstance(out, list), "Layer output should be a list of Value objects"
    assert len(out) == 2, "Layer output length should match number of neurons"

def test_layer_backward():
    l = Layer(2, 2)
    x = [Value(1.0), Value(-1.0)]
    out = l(x)
    # sum outputs to create a scalar for backward
    loss = sum(out)
    loss.backward()
    # each weight and bias should have a gradient
    for n in l.neurons:
        for p in n.parameters():
            assert p.grad != 0.0, "Parameter gradient should not be zero after backward"

# -----------------------------
# MLP Tests
# -----------------------------
def test_mlp_forward():
    mlp = MLP(3, [4, 2, 1])  # 3 inputs, 3 layers
    x = [Value(1.0), Value(2.0), Value(-1.0)]
    out = mlp(x)
    assert isinstance(out, Value), "MLP output should be a Value object (single output)"

def test_mlp_backward():
    mlp = MLP(2, [2, 1])  # 2 inputs, 2 layers
    x = [Value(1.0), Value(-1.0)]
    out = mlp(x)
    out.backward()
    # check that all parameters have non-zero gradients
    for p in mlp.parameters():
        assert p.grad != 0.0, "MLP parameter gradient should not be zero after backward"

# -----------------------------
# Gradient zeroing test
# -----------------------------
def test_mlp_zero_grad():
    mlp = MLP(2, [2, 1])
    x = [Value(1.0), Value(-1.0)]
    out = mlp(x)
    out.backward()
    mlp.zero_grad()
    # all gradients should be reset to zero
    for p in mlp.parameters():
        assert p.grad == 0.0, "Gradients should be zero after zero_grad()"