class RedBlackTree {

    // Enum-like constants for colors
    private static final boolean RED = true;
    private static final boolean BLACK = false;

    // Node structure
    static class Node {
        int data;
        Node left, right, parent;
        boolean color; // true = RED, false = BLACK

        Node(int data) {
            this.data = data;
            color = RED;
            left = right = parent = null;
        }
    }

    private Node root;

    // Utility function to perform left rotation
    private void leftRotate(Node x) {
        Node y = x.right;
        x.right = y.left;

        if (y.left != null)
            y.left.parent = x;

        y.parent = x.parent;

        if (x.parent == null)
            root = y;
        else if (x == x.parent.left)
            x.parent.left = y;
        else
            x.parent.right = y;

        y.left = x;
        x.parent = y;
    }

    // Utility function to perform right rotation
    private void rightRotate(Node y) {
        Node x = y.left;
        y.left = x.right;

        if (x.right != null)
            x.right.parent = y;

        x.parent = y.parent;

        if (y.parent == null)
            root = x;
        else if (y == y.parent.left)
            y.parent.left = x;
        else
            y.parent.right = x;

        x.right = y;
        y.parent = x;
    }

    // Fix violations after insertion
    private void fixViolation(Node pt) {
        Node parentPt = null;
        Node grandParentPt = null;

        while (pt != root && pt.color == RED && pt.parent.color == RED) {
            parentPt = pt.parent;
            grandParentPt = parentPt.parent;

            // Case A: Parent is left child of grandparent
            if (parentPt == grandParentPt.left) {
                Node unclePt = grandParentPt.right;

                // Case 1: Uncle is RED → Recolor
                if (unclePt != null && unclePt.color == RED) {
                    grandParentPt.color = RED;
                    parentPt.color = BLACK;
                    unclePt.color = BLACK;
                    pt = grandParentPt;
                } else {
                    // Case 2: pt is right child → Left rotate
                    if (pt == parentPt.right) {
                        leftRotate(parentPt);
                        pt = parentPt;
                        parentPt = pt.parent;
                    }

                    // Case 3: pt is left child → Right rotate
                    rightRotate(grandParentPt);
                    boolean temp = parentPt.color;
                    parentPt.color = grandParentPt.color;
                    grandParentPt.color = temp;
                    pt = parentPt;
                }
            }

            // Case B: Parent is right child of grandparent
            else {
                Node unclePt = grandParentPt.left;

                // Case 1: Uncle is RED → Recolor
                if (unclePt != null && unclePt.color == RED) {
                    grandParentPt.color = RED;
                    parentPt.color = BLACK;
                    unclePt.color = BLACK;
                    pt = grandParentPt;
                } else {
                    // Case 2: pt is left child → Right rotate
                    if (pt == parentPt.left) {
                        rightRotate(parentPt);
                        pt = parentPt;
                        parentPt = pt.parent;
                    }

                    // Case 3: pt is right child → Left rotate
                    leftRotate(grandParentPt);
                    boolean temp = parentPt.color;
                    parentPt.color = grandParentPt.color;
                    grandParentPt.color = temp;
                    pt = parentPt;
                }
            }
        }

        root.color = BLACK; // Root is always black
    }

    // Insert a new node
    public void insert(int data) {
        Node pt = new Node(data);
        root = bstInsert(root, pt);
        fixViolation(pt);
    }

    // Normal BST insertion
    private Node bstInsert(Node root, Node pt) {
        if (root == null)
            return pt;

        if (pt.data < root.data) {
            root.left = bstInsert(root.left, pt);
            root.left.parent = root;
        } else if (pt.data > root.data) {
            root.right = bstInsert(root.right, pt);
            root.right.parent = root;
        }

        return root;
    }

    // Inorder traversal
    public void inorder() {
        inorderHelper(root);
        System.out.println();
    }

    private void inorderHelper(Node node) {
        if (node == null)
            return;
        inorderHelper(node.left);
        System.out.print(node.data + (node.color == RED ? "(R) " : "(B) "));
        inorderHelper(node.right);
    }

    // Main method to test
    public static void main(String[] args) {
        RedBlackTree tree = new RedBlackTree();
        int[] values = {10, 20, 30, 15, 25, 5, 1};

        for (int val : values) {
            tree.insert(val);
            System.out.print("After inserting " + val + ": ");
            tree.inorder();
        }

        System.out.println("\nFinal Red-Black Tree (Inorder Traversal):");
        tree.inorder();
    }
}