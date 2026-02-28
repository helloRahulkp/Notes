class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Build tree interactively
def build_tree():
    value = int(input("Enter node value (-1 to stop): "))
    if value == -1:
        return None

    root = Node(value)
    print(f"Left child of {value}")
    root.left = build_tree()
    print(f"Right child of {value}")
    root.right = build_tree()
    return root

# Traversals
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

def get_width(root, level):
    if root is None:
        return 0
    if level == 1:
        return 1
    return get_width(root.left, level - 1) + get_width(root.right, level - 1)

def max_width(root):
    h = height(root)
    max_w = 0
    for i in range(1, h + 1):
        width = get_width(root, i)
        if width > max_w:
            max_w = width
    return max_w

# Driver code
if __name__ == "__main__":
    root = build_tree()

    print("Preorder:", end=" ")
    preorder(root)
    print("\nInorder:", end=" ")
    inorder(root)
    print("\nPostorder:", end=" ")
    postorder(root)

    print("\n\nMaximum Width of Tree:", max_width(root))