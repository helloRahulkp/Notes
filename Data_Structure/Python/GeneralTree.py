class Node:
    def __init__(self, data, child_count):
        self.data = data
        self.child_count = child_count
        self.children = [None] * child_count

# Print tree (Preorder)
def print_tree(root):
    if root is None:
        return
    print(root.data, end=" ")
    for child in root.children:
        print_tree(child)

# Example usage
root = Node(1, 3)
root.children[0] = Node(2, 0)
root.children[1] = Node(3, 2)
root.children[1].children[0] = Node(4, 0)
root.children[1].children[1] = Node(5, 0)
root.children[2] = Node(6, 0)

print("General Tree Preorder:", end=" ")
print_tree(root)