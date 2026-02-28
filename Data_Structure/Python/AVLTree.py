class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially a leaf


class AVLTree:
    # Get height of the node
    def height(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotation
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x  # New root

    # Left rotation
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y  # New root

    # Insert a key
    def insert(self, root, key):
        # 1. Perform normal BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicates not allowed

        # 2. Update height
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # 3. Get balance factor
        balance = self.get_balance(root)

        # 4. Balance the tree (4 cases)
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Find node with minimum key value
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # Delete a node
    def delete(self, root, key):
        # 1. Perform standard BST delete
        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            # Node with one or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # If the tree had only one node
        if root is None:
            return root

        # 2. Update height
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # 3. Balance
        balance = self.get_balance(root)

        # 4. Balance cases
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search for a key
    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    # Traversals
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# --- Main Program ---
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    while True:
        print("\n--- AVL Tree Operations ---")
        print("1. Insert\n2. Delete\n3. Search\n4. Inorder\n5. Preorder\n6. Postorder\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = int(input("Enter key to insert: "))
            root = tree.insert(root, key)

        elif choice == 2:
            key = int(input("Enter key to delete: "))
            root = tree.delete(root, key)

        elif choice == 3:
            key = int(input("Enter key to search: "))
            if tree.search(root, key):
                print(f"{key} found in the tree.")
            else:
                print(f"{key} not found.")

        elif choice == 4:
            print("Inorder traversal:", end=" ")
            tree.inorder(root)
            print()

        elif choice == 5:
            print("Preorder traversal:", end=" ")
            tree.preorder(root)
            print()

        elif choice == 6:
            print("Postorder traversal:", end=" ")
            tree.postorder(root)
            print()

        elif choice == 7:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")