import math
import pytest
from micrograd.engine import Value

# -----------------------------
# Test basic arithmetic
# -----------------------------
def test_addition():
    a = Value(2.0)
    b = Value(3.0)
    c = a + b
    assert c.data == 5.0
    c.backward()
    assert a.grad == 1.0
    assert b.grad == 1.0

def test_subtraction():
    a = Value(5.0)
    b = Value(3.0)
    c = a - b
    assert c.data == 2.0
    c.backward()
    assert a.grad == 1.0
    assert b.grad == -1.0

def test_multiplication():
    a = Value(2.0)
    b = Value(4.0)
    c = a * b
    assert c.data == 8.0
    c.backward()
    assert a.grad == 4.0
    assert b.grad == 2.0

def test_division():
    a = Value(8.0)
    b = Value(2.0)
    c = a / b
    assert c.data == 4.0
    c.backward()
    assert a.grad == 0.5  # dc/da = 1/b
    assert b.grad == -2.0  # dc/db = -a/b^2

def test_power():
    a = Value(3.0)
    c = a ** 2
    assert c.data == 9.0
    c.backward()
    assert a.grad == 6.0  # dc/da = 2*a

# -----------------------------
# Test activation functions
# -----------------------------
def test_tanh():
    a = Value(0.0)
    t = a.tanh()
    assert math.isclose(t.data, 0.0)
    t.backward()
    assert math.isclose(a.grad, 1.0)

def test_relu():
    a = Value(-1.0)
    r = a.relu()
    assert r.data == 0.0
    r.backward()
    assert a.grad == 0.0

    b = Value(2.0)
    r2 = b.relu()
    assert r2.data == 2.0
    r2.backward()
    assert b.grad == 1.0

def test_exp():
    a = Value(1.0)
    e = a.exp()
    assert math.isclose(e.data, math.exp(1.0))
    e.backward()
    assert math.isclose(a.grad, math.exp(1.0))

# -----------------------------
# Test chained operations and backward
# -----------------------------
def test_chain_operations():
    a = Value(2.0)
    b = Value(3.0)
    c = a * b + a + b
    c.backward()
    # dc/da = b + 1 = 4
    assert a.grad == 4.0
    # dc/db = a + 1 = 3
    assert b.grad == 2.0 + 1.0  # a + 1