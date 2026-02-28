from graphviz import Digraph


def trace(root):
    """
    Builds a set of all nodes and edges in the computational graph.

    Args:
        root: Value object (root of the graph)

    Returns:
        nodes: set of all Value nodes
        edges: set of edges (parent, child) in the graph
    """
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)

    build(root)
    return nodes, edges


def draw_dot(root):
    """
    Draws the computational graph of a Value object using Graphviz.

    Args:
        root: Value object (root of the graph)

    Returns:
        dot: Graphviz Digraph object
    """
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
    nodes, edges = trace(root)

    # Create nodes
    for n in nodes:
        uid = str(id(n))
        dot.node(
            name=uid,
            label="{ %s | data %.4f | grad %.4f }" % (n.label, n.data, n.grad),
            shape='record'
        )

        if n._op:
            # Create operation node
            dot.node(uid + n._op, label=n._op)
            dot.edge(uid + n._op, uid)

    # Create edges
    for n1, n2 in edges:
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot



# utils.py for visualization and dataset generation
from sklearn.datasets import make_moons

def draw_dot(root, filename="graph"):
    from graphviz import Digraph
    # ... (use your existing draw_dot code) ...
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
    # ... build nodes and edges ...
    return dot

def make_moons_dataset(n_samples=200, noise=0.1):
    X, y = make_moons(n_samples=n_samples, noise=noise)
    return X, y