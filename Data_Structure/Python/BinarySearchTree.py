class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        if key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

# Usage
tree = BST()
root = None

print("Enter values to insert into BST (-1 to stop):")
while True:
    value = int(input())
    if value == -1:
        break
    root = tree.insert(root, value)

print("Inorder Traversal:", end=" ")
tree.inorder(root)
print()

key = int(input("Enter value to search: "))
if tree.search(root, key):
    print(f"{key} found in BST.")
else:
    print(f"{key} not found in BST.")