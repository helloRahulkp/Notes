class Node {
    int data;
    int childCount;
    Node[] children;

    Node(int data, int childCount){
        this.data = data;
        this.childCount = childCount;
        this.children = new Node[childCount];
    }
}

public class GeneralTree {
    static void printTree(Node root){
        if (root == null) return;
        System.out.print(root.data + " ");
        for (Node child : root.children){
            printTree(child);
        }
    }

    public static void main(String[] args){

        Node root = new Node(1, 3);
        root.children[0] = new Node(2, 0);
        root.children[1] = new Node(3, 2);
        root.children[1].children[0] = new Node(4, 0);
        root.children[1].children[1] = new Node(5, 0);
        root.children[2] = new Node(6, 0);

        System.out.print("General Tree Preorder: ");
        printTree(root);
    }
}