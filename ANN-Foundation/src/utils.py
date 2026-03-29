import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons


def make_moons_dataset(n_samples=200, noise=0.1):
    return make_moons(n_samples=n_samples, noise=noise)


def plot_decision_boundary(model, X, y):
    h = 0.05
    x_min, x_max = X[:, 0].min()-1, X[:, 0].max()+1
    y_min, y_max = X[:, 1].min()-1, X[:, 1].max()+1

    xx, yy = np.meshgrid(
        np.arange(x_min, x_max, h),
        np.arange(y_min, y_max, h)
    )

    grid = np.c_[xx.ravel(), yy.ravel()]
    preds = [model(list(p)).data for p in grid]
    Z = np.array(preds).reshape(xx.shape)

    plt.contourf(xx, yy, Z > 0, alpha=0.5)
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.title("Decision Boundary")
    plt.show()