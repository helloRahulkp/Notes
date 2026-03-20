from micrograd.engine import Value


def test_add():
    a, b = Value(2), Value(3)
    c = a + b
    c.backward()
    assert c.data == 5
    assert a.grad == 1
    assert b.grad == 1


def test_mul():
    a, b = Value(2), Value(4)
    c = a * b
    c.backward()
    assert a.grad == 4
    assert b.grad == 2