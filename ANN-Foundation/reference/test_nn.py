from micrograd.nn import MLP


def test_mlp_forward():
    model = MLP(3, [4, 1])
    out = model([1.0, 2.0, 3.0])
    assert out is not None