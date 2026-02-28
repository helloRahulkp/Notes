# Micrograd: Mini Autograd Engine in Python

A lightweight, educational **autograd engine and neural network library** implemented in pure Python. Inspired by micrograd, this project allows you to understand and experiment with the inner workings of backpropagation, forward and backward passes, and simple neural network training without external deep learning frameworks.

This project is structured for clarity, modularity, and testing, making it perfect for learning, experimentation, and small-scale neural network projects.

---

## 🏗 Project Structure

ANN Foundation/
├── notebooks/
│ ├── foundation.ipynb
│ ├── micrograd_lecture_first_half_roughly.ipynb
│ └── micrograd_lecture_second_half_roughly.ipynb
├── src/
│ └── micrograd/
│ ├── init.py
│ ├── engine.py # Core Value class and autograd logic
│ ├── nn.py # Neuron, Layer, MLP classes
│ └── utils.py # Utility functions like draw_dot
├── test/
│ ├── test_engine.py # Unit tests for Value class and autograd
│ └── test_nn.py # Unit tests for Neuron, Layer, and MLP
├── data/ # Optional datasets for experiments
├── README.md
├── requirements.txt
└── .gitignore

---

## ⚡ Features

- **Autograd Engine (`Value`)**
  - Forward and backward propagation
  - Supports addition, subtraction, multiplication, division, power
  - Common activations: `tanh`, `ReLU`, `exp`
  - Graph visualization via `graphviz`

- **Neural Networks**
  - `Neuron`, `Layer`, and `MLP` classes
  - Fully differentiable with `Value`
  - Manual and automatic gradient calculation
  - Training with gradient descent

- **Utilities**
  - `draw_dot`: Visualize computation graphs
  - Helper functions for experiments and visualization

- **Testing**
  - Unit tests for engine and neural network classes
  - Forward and backward pass coverage

---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd "ANN Foundation"
```

Create a virtual environment and activate it:

python -m venv .venv
source .venv/bin/activate # macOS / Linux
.venv\Scripts\activate # Windows

Install dependencies:
pip install -r requirements.txt

(Optional) Make micrograd package importable:
pip install -e ./src

🧪 Running Tests

Run all tests with pytest:
PYTHONPATH=src pytest test/test_engine.py
PYTHONPATH=src pytest test/test_nn.py

If installed in editable mode:
pytest test/test_engine.py
pytest test/test_nn.py

📖 Example Usage
from micrograd.engine import Value
from micrograd.utils import draw_dot

# Define computation

a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = a \* b; c.label = 'c'
d = c + a; d.label = 'd'

# Backpropagate

d.backward()

# Visualize computation graph

dot = draw_dot(d)
dot.render('graph', view=True)

from micrograd.nn import Neuron, Layer, MLP

# Single neuron forward

n = Neuron(2)
x = [Value(1.0), Value(-2.0)]
output = n(x)
output.backward()

# Multi-layer MLP

mlp = MLP(3, [4, 2, 1])
x = [Value(1.0), Value(2.0), Value(-1.0)]
y = mlp(x)
y.backward()

📚 Learning Goals

Understand autograd and computation graphs

Learn forward and backward propagation manually

Implement a mini neural network library from scratch

Visualize computation and gradients

🛠 Tech Stack

Python 3.10+

NumPy

Matplotlib

Graphviz

🔗 References

micrograd by Andrej Karpathy

Deep Learning concepts: forward/backward propagation, chain rule

Educational purposes for AI/ML understanding
