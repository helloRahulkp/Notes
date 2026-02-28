class Node:
    RED = True
    BLACK = False

    def __init__(self, data):
        self.data = data
        self.color = Node.RED  # New nodes are red by default
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right:
            x.right.parent = y

        x.parent = y.parent
        if not y.parent:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    # Fix Red-Black violations after insertion
    def fix_violation(self, pt):
        while pt != self.root and pt.parent.color == Node.RED:
            parent = pt.parent
            grandparent = parent.parent

            # Parent is left child
            if parent == grandparent.left:
                uncle = grandparent.right

                # Case 1: Uncle is red → recolor
                if uncle and uncle.color == Node.RED:
                    grandparent.color = Node.RED
                    parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    pt = grandparent
                else:
                    # Case 2: pt is right child → left rotate
                    if pt == parent.right:
                        self.left_rotate(parent)
                        pt = parent
                        parent = pt.parent

                    # Case 3: pt is left child → right rotate
                    self.right_rotate(grandparent)
                    parent.color, grandparent.color = grandparent.color, parent.color
                    pt = parent

            # Parent is right child
            else:
                uncle = grandparent.left

                if uncle and uncle.color == Node.RED:
                    grandparent.color = Node.RED
                    parent.color = Node.BLACK
                    uncle.color = Node.BLACK
                    pt = grandparent
                else:
                    if pt == parent.left:
                        self.right_rotate(parent)
                        pt = parent
                        parent = pt.parent

                    self.left_rotate(grandparent)
                    parent.color, grandparent.color = grandparent.color, parent.color
                    pt = parent

        self.root.color = Node.BLACK

    # BST insert
    def bst_insert(self, root, pt):
        if not root:
            return pt

        if pt.data < root.data:
            root.left = self.bst_insert(root.left, pt)
            root.left.parent = root
        elif pt.data > root.data:
            root.right = self.bst_insert(root.right, pt)
            root.right.parent = root

        return root

    # Main insert
    def insert(self, data):
        new_node = Node(data)
        self.root = self.bst_insert(self.root, new_node)
        self.fix_violation(new_node)

    # Inorder traversal
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder(node.left)
        print(f"{node.data}({'R' if node.color == Node.RED else 'B'})", end=" ")
        if node.right:
            self.inorder(node.right)


# Example usage
if __name__ == "__main__":
    rbt = RedBlackTree()
    values = [10, 20, 30, 15, 25, 5, 1]

    for val in values:
        rbt.insert(val)
        print(f"After inserting {val}: ", end="")
        rbt.inorder()
        print()

    print("\nFinal Red-Black Tree (Inorder Traversal):")
    rbt.inorder()
    print()