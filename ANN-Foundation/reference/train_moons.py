from micrograd.nn import MLP
from micrograd.utils import make_moons_dataset, plot_decision_boundary

X, y = make_moons_dataset(200, noise=0.2)
y = y * 2 - 1

model = MLP(2, [16, 16, 1])

for epoch in range(50):
    loss_total = 0

    for xi, yi in zip(X, y):
        pred = model(list(xi))
        loss = (pred - yi)**2

        model.zero_grad()
        loss.backward()

        for p in model.parameters():
            p.data += -0.05 * p.grad

        loss_total += loss.data

    print(f"Epoch {epoch}: Loss {loss_total:.4f}")

plot_decision_boundary(model, X, y)