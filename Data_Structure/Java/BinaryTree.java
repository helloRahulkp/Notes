import java.util.Scanner;

class Node {
    int data;
    Node left, right;

    Node(int item) {
        data = item;
        left = right = null;
    }
}

public class BinaryTree {
    Scanner sc = new Scanner(System.in);

    // Build tree interactively
    Node buildTree() {
        System.out.print("Enter node value (-1 to stop): ");
        int value = sc.nextInt();
        if (value == -1) return null;

        Node root = new Node(value);

        System.out.println("Left child of " + value);
        root.left = buildTree();

        System.out.println("Right child of " + value);
        root.right = buildTree();

        return root;
    }

    // Traversals
    void preorder(Node root) {
        if (root == null) return;
        System.out.print(root.data + " ");
        preorder(root.left);
        preorder(root.right);
    }

    void inorder(Node root) {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.data + " ");
        inorder(root.right);
    }

    void postorder(Node root) {
        if (root == null) return;
        postorder(root.left);
        postorder(root.right);
        System.out.print(root.data + " ");
    }

    int height(Node root) {
        if (root == null) return 0;
        return Math.max(height(root.left), height(root.right)) + 1;
    }

    int getWidth(Node root, int level) {
        if (root == null) return 0;
        if (level == 1) return 1;
        return getWidth(root.left, level - 1) + getWidth(root.right, level - 1);
    }

    int getMaxWidth(Node root) {
        int maxWidth = 0;
        int h = height(root);
        for (int i = 1; i <= h; i++) {
            int width = getWidth(root, i);
            if (width > maxWidth) maxWidth = width;
        }
        return maxWidth;
    }

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        Node root = tree.buildTree();

        System.out.print("Preorder: ");
        tree.preorder(root);
        System.out.print("\nInorder: ");
        tree.inorder(root);
        System.out.print("\nPostorder: ");
        tree.postorder(root);

        System.out.println("\n\nMaximum Width of Tree: " + tree.getMaxWidth(root));
    }
}