import java.util.Scanner;

class BSTNode {
    int data;
    BSTNode left, right;
    BSTNode(int value) {
        data = value;
        left = right = null;
    }
}

class BinarySearchTree {
    BSTNode root;

    BSTNode insert(BSTNode root, int data) {
        if (root == null) return new BSTNode(data);
        if (data < root.data) root.left = insert(root.left, data);
        else if (data > root.data) root.right = insert(root.right, data);
        return root;
    }

    BSTNode search(BSTNode root, int key) {
        if (root == null || root.data == key) return root;
        if (key < root.data) return search(root.left, key);
        else return search(root.right, key);
    }

    void inorder(BSTNode root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.data + " ");
            inorder(root.right);
        }
    }

    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        Scanner sc = new Scanner(System.in);
        int value, key;

        System.out.println("Enter values to insert into BST (-1 to stop):");
        while (true) {
            value = sc.nextInt();
            if (value == -1) break;
            tree.root = tree.insert(tree.root, value);
        }

        System.out.print("Inorder Traversal: ");
        tree.inorder(tree.root);
        System.out.println();

        System.out.print("Enter value to search: ");
        key = sc.nextInt();

        if (tree.search(tree.root, key) != null)
            System.out.println(key + " found in BST.");
        else
            System.out.println(key + " not found in BST.");

        sc.close();
    }
}