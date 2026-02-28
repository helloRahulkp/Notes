# # problem.py
# import numpy as np
# import matplotlib.pyplot as plt
# import pickle
# import random

# from micrograd.engine import Value
# from micrograd.nn import MLP
# from micrograd.utils import draw_dot, make_moons_dataset

# # --- Seed for reproducibility ---
# np.random.seed(1337)
# random.seed(1337)

# # --- Dataset ---
# X, y = make_moons_dataset(n_samples=200, noise=0.1)
# y = y*2 - 1  # convert to -1 or 1

# # --- Initialize Model ---
# model = MLP(2, [16, 16, 1])
# print("Model initialized. Number of parameters:", len(model.parameters()))

# # --- Check if weights exist ---
# WEIGHTS_FILE = "mlp_weights.pkl"
# try:
#     with open(WEIGHTS_FILE, "rb") as f:
#         loaded_params = pickle.load(f)
#     for p, val in zip(model.parameters(), loaded_params):
#         p.data = val
#     print("Loaded saved weights and biases!")
# except FileNotFoundError:
#     print("Weights not found. Training model from scratch...")

#     # --- Training parameters ---
#     def loss(batch_size=None):
#         if batch_size is None:
#             Xb, yb = X, y
#         else:
#             ri = np.random.permutation(X.shape[0])[:batch_size]
#             Xb, yb = X[ri], y[ri]

#         inputs = [list(map(Value, xrow)) for xrow in Xb]
#         scores = list(map(model, inputs))
#         losses = [(1 + -yi * scorei).relu() for yi, scorei in zip(yb, scores)]
#         data_loss = sum(losses) * (1.0 / len(losses))
#         alpha = 1e-4
#         reg_loss = alpha * sum((p*p for p in model.parameters()))
#         total_loss = data_loss + reg_loss
#         accuracy = [(yi > 0) == (scorei.data > 0) for yi, scorei in zip(yb, scores)]
#         return total_loss, sum(accuracy) / len(accuracy)

#     # --- Training loop ---
#     for k in range(100):
#         total_loss, acc = loss()
#         model.zero_grad()
#         total_loss.backward()

#         learning_rate = 1.0 - 0.9*k/100
#         for p in model.parameters():
#             p.data -= learning_rate * p.grad

#         if k % 1 == 0:
#             print(f"Step {k}: loss={total_loss.data}, accuracy={acc*100:.2f}%")

#     # --- Save trained weights ---
#     params_data = [p.data for p in model.parameters()]
#     with open(WEIGHTS_FILE, "wb") as f:
#         pickle.dump(params_data, f)
#     print("Weights saved to", WEIGHTS_FILE)

# # --- Visualize Decision Boundary ---
# h = 0.10
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                      np.arange(y_min, y_max, h))
# Xmesh = np.c_[xx.ravel(), yy.ravel()]
# inputs = [list(map(Value, xrow)) for xrow in Xmesh]
# scores = list(map(model, inputs))
# Z = np.array([s.data > 0 for s in scores]).reshape(xx.shape)

# plt.figure(figsize=(6,6))
# plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
# plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())
# plt.title("Decision Boundary")
# plt.show()


# problem.py
import numpy as np
import matplotlib.pyplot as plt
import pickle
import random
import os

from micrograd.engine import Value
from micrograd.nn import MLP
from micrograd.utils import draw_dot, make_moons_dataset

# --- Seed for reproducibility ---
np.random.seed(1337)
random.seed(1337)

# --- Dataset ---
X, y = make_moons_dataset(n_samples=200, noise=0.1)
y = y*2 - 1  # convert to -1 or 1

# --- Initialize Model ---
model = MLP(2, [16, 16, 1])
print("Model initialized. Number of parameters:", len(model.parameters()))

# --- Weights file ---
WEIGHTS_FILE = "mlp_weights.pkl"

# --- Function to load weights ---
def load_weights(model, filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            loaded_params = pickle.load(f)
        for p, val in zip(model.parameters(), loaded_params):
            p.data = val
        print("✅ Loaded saved weights!")
        return True
    return False

# --- Function to save weights ---
def save_weights(model, filename):
    params_data = [p.data for p in model.parameters()]
    with open(filename, "wb") as f:
        pickle.dump(params_data, f)
    print("✅ Saved weights to", filename)

# --- Check for saved weights first ---
if not load_weights(model, WEIGHTS_FILE):
    print("Weights not found. Training model from scratch...")

    # --- Loss function ---
    def compute_loss(Xb, yb, model):
        inputs = [list(map(Value, xrow)) for xrow in Xb]
        scores = list(map(model, inputs))
        losses = [(1 - yi*scorei).relu() for yi, scorei in zip(yb, scores)]
        data_loss = sum(losses) * (1.0 / len(losses))
        alpha = 1e-4
        reg_loss = alpha * sum((p*p for p in model.parameters()))
        total_loss = data_loss + reg_loss
        accuracy = [(yi > 0) == (scorei.data > 0) for yi, scorei in zip(yb, scores)]
        return total_loss, sum(accuracy) / len(accuracy)

    # --- Training loop ---
    for k in range(100):
        total_loss, acc = compute_loss(X, y, model)
        model.zero_grad()
        total_loss.backward()

        learning_rate = 1.0 - 0.9*k/100
        for p in model.parameters():
            p.data -= learning_rate * p.grad

        if k % 10 == 0:
            print(f"Step {k}: loss={total_loss.data:.4f}, accuracy={acc*100:.2f}%")

    save_weights(model, WEIGHTS_FILE)
else:
    # --- If weights loaded, compute accuracy directly ---
    inputs = [list(map(Value, xrow)) for xrow in X]
    scores = list(map(model, inputs))
    acc = [(yi > 0) == (s.data > 0) for yi, s in zip(y, scores)]
    print(f"Accuracy using loaded weights: {sum(acc)/len(acc)*100:.2f}%")

# --- Visualize Decision Boundary ---
h = 0.10
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
Xmesh = np.c_[xx.ravel(), yy.ravel()]
inputs = [list(map(Value, xrow)) for xrow in Xmesh]
scores = list(map(model, inputs))
Z = np.array([s.data > 0 for s in scores]).reshape(xx.shape)

plt.figure(figsize=(6,6))
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, cmap=plt.cm.Spectral)
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.title("Decision Boundary")
plt.show()