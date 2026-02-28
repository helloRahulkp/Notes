"""
Autograde: A minimal automatic differentiation engine
and neural network library inspired by micrograd.
"""

# Core Autograd Engine
from .engine import Value

# Neural Network Components
from .nn import Neuron, Layer, MLP

# Utilities (Visualization and Helpers)
from .utils import trace, draw_dot

# Public API
__all__ = [
    "Value",
    "Neuron",
    "Layer",
    "MLP",
    "trace",
    "draw_dot",
]