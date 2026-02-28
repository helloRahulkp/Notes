import java.util.Scanner;

// Define Node structure for AVL Tree
class Node {
    int key, height;
    Node left, right;

    Node(int d) {
        key = d;
        height = 1; // new node is initially added at leaf
    }
}

public class AVLTree {

    Node root;

    // Get height of a node
    int height(Node N) {
        if (N == null)
            return 0;
        return N.height;
    }

    // Get maximum of two numbers
    int max(int a, int b) {
        return (a > b) ? a : b;
    }

    // Right rotate
    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;

        // Return new root
        return x;
    }

    // Left rotate
    Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        // Perform rotation
        y.left = x;
        x.right = T2;

        // Update heights
        x.height = max(height(x.left), height(x.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;

        // Return new root
        return y;
    }

    // Get Balance Factor
    int getBalance(Node N) {
        if (N == null)
            return 0;
        return height(N.left) - height(N.right);
    }

    // Insert node into AVL tree
    Node insert(Node node, int key) {
        // 1. Normal BST insertion
        if (node == null)
            return new Node(key);

        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else
            return node; // duplicates not allowed

        // 2. Update height
        node.height = 1 + max(height(node.left), height(node.right));

        // 3. Get balance factor
        int balance = getBalance(node);

        // 4. Balance the tree

        // Left Left Case
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node; // unchanged
    }

    // Get minimum value node
    Node minValueNode(Node node) {
        Node current = node;
        while (current.left != null)
            current = current.left;
        return current;
    }

    // Delete node
    Node deleteNode(Node root, int key) {
        // 1. Normal BST deletion
        if (root == null)
            return root;

        if (key < root.key)
            root.left = deleteNode(root.left, key);
        else if (key > root.key)
            root.right = deleteNode(root.right, key);
        else {
            // Node with one or no child
            if ((root.left == null) || (root.right == null)) {
                Node temp = (root.left != null) ? root.left : root.right;

                if (temp == null) { // no child
                    temp = root;
                    root = null;
                } else
                    root = temp; // one child
            } else {
                // Node with two children
                Node temp = minValueNode(root.right);
                root.key = temp.key;
                root.right = deleteNode(root.right, temp.key);
            }
        }

        // If tree had only one node
        if (root == null)
            return root;

        // 2. Update height
        root.height = max(height(root.left), height(root.right)) + 1;

        // 3. Get balance factor
        int balance = getBalance(root);

        // 4. Balance the tree
        if (balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);

        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }

        if (balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);

        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }

        return root;
    }

    // Search
    Node search(Node root, int key) {
        if (root == null || root.key == key)
            return root;
        if (key < root.key)
            return search(root.left, key);
        return search(root.right, key);
    }

    // Traversals
    void inorder(Node root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.key + " ");
            inorder(root.right);
        }
    }

    void preorder(Node root) {
        if (root != null) {
            System.out.print(root.key + " ");
            preorder(root.left);
            preorder(root.right);
        }
    }

    void postorder(Node root) {
        if (root != null) {
            postorder(root.left);
            postorder(root.right);
            System.out.print(root.key + " ");
        }
    }

    // Interactive menu
    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
        Scanner sc = new Scanner(System.in);
        int choice, key;

        while (true) {
            System.out.println("\n--- AVL Tree Operations ---");
            System.out.println("1. Insert\n2. Delete\n3. Search\n4. Inorder\n5. Preorder\n6. Postorder\n7. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter key to insert: ");
                    key = sc.nextInt();
                    tree.root = tree.insert(tree.root, key);
                    break;

                case 2:
                    System.out.print("Enter key to delete: ");
                    key = sc.nextInt();
                    tree.root = tree.deleteNode(tree.root, key);
                    break;

                case 3:
                    System.out.print("Enter key to search: ");
                    key = sc.nextInt();
                    if (tree.search(tree.root, key) != null)
                        System.out.println(key + " found in the tree.");
                    else
                        System.out.println(key + " not found.");
                    break;

                case 4:
                    System.out.print("Inorder traversal: ");
                    tree.inorder(tree.root);
                    System.out.println();
                    break;

                case 5:
                    System.out.print("Preorder traversal: ");
                    tree.preorder(tree.root);
                    System.out.println();
                    break;

                case 6:
                    System.out.print("Postorder traversal: ");
                    tree.postorder(tree.root);
                    System.out.println();
                    break;

                case 7:
                    System.out.println("Exiting...");
                    sc.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid choice!");
            }
        }
    }
}