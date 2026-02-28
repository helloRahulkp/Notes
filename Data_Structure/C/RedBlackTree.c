#include <stdio.h>
#include <stdlib.h>

// Enum for node color
typedef enum { RED, BLACK } Color;

// Structure for a Red-Black Tree node
typedef struct Node {
    int data;
    Color color;
    struct Node *left, *right, *parent;
} Node;

// Function to create a new node
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->color = RED; // New nodes are always red
    newNode->left = newNode->right = newNode->parent = NULL;
    return newNode;
}

// Utility function to perform left rotation
Node* leftRotate(Node* root, Node* x) {
    Node* y = x->right;
    x->right = y->left;

    if (y->left != NULL)
        y->left->parent = x;

    y->parent = x->parent;

    if (x->parent == NULL)
        root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;

    y->left = x;
    x->parent = y;

    return root;
}

// Utility function to perform right rotation
Node* rightRotate(Node* root, Node* y) {
    Node* x = y->left;
    y->left = x->right;

    if (x->right != NULL)
        x->right->parent = y;

    x->parent = y->parent;

    if (y->parent == NULL)
        root = x;
    else if (y == y->parent->left)
        y->parent->left = x;
    else
        y->parent->right = x;

    x->right = y;
    y->parent = x;

    return root;
}

// Function to fix Red-Black Tree violations after insertion
Node* fixViolation(Node* root, Node* pt) {
    Node* parent_pt = NULL;
    Node* grand_parent_pt = NULL;

    while ((pt != root) && (pt->color == RED) &&
           (pt->parent->color == RED)) {

        parent_pt = pt->parent;
        grand_parent_pt = parent_pt->parent;

        // Case A: Parent is left child of grandparent
        if (parent_pt == grand_parent_pt->left) {
            Node* uncle_pt = grand_parent_pt->right;

            // Case 1: Uncle is red → Recolor
            if (uncle_pt != NULL && uncle_pt->color == RED) {
                grand_parent_pt->color = RED;
                parent_pt->color = BLACK;
                uncle_pt->color = BLACK;
                pt = grand_parent_pt;
            } else {
                // Case 2: pt is right child → Left rotate
                if (pt == parent_pt->right) {
                    root = leftRotate(root, parent_pt);
                    pt = parent_pt;
                    parent_pt = pt->parent;
                }

                // Case 3: pt is left child → Right rotate
                root = rightRotate(root, grand_parent_pt);

                // Swap colors
                Color temp = parent_pt->color;
                parent_pt->color = grand_parent_pt->color;
                grand_parent_pt->color = temp;

                pt = parent_pt;
            }
        }

        // Case B: Parent is right child of grandparent
        else {
            Node* uncle_pt = grand_parent_pt->left;

            // Case 1: Uncle is red → Recolor
            if (uncle_pt != NULL && uncle_pt->color == RED) {
                grand_parent_pt->color = RED;
                parent_pt->color = BLACK;
                uncle_pt->color = BLACK;
                pt = grand_parent_pt;
            } else {
                // Case 2: pt is left child → Right rotate
                if (pt == parent_pt->left) {
                    root = rightRotate(root, parent_pt);
                    pt = parent_pt;
                    parent_pt = pt->parent;
                }

                // Case 3: pt is right child → Left rotate
                root = leftRotate(root, grand_parent_pt);

                // Swap colors
                Color temp = parent_pt->color;
                parent_pt->color = grand_parent_pt->color;
                grand_parent_pt->color = temp;

                pt = parent_pt;
            }
        }
    }

    root->color = BLACK; // Root is always black
    return root;
}

// Utility function to insert into BST and then fix RBT property
Node* insertBST(Node* root, Node* pt) {
    if (root == NULL)
        return pt;

    if (pt->data < root->data) {
        root->left = insertBST(root->left, pt);
        root->left->parent = root;
    } else if (pt->data > root->data) {
        root->right = insertBST(root->right, pt);
        root->right->parent = root;
    }
    return root;
}

// Main insertion function
Node* insert(Node* root, int data) {
    Node* pt = createNode(data);
    root = insertBST(root, pt);
    root = fixViolation(root, pt);
    return root;
}

// Inorder traversal to display the tree
void inorder(Node* root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d(%s) ", root->data, root->color == RED ? "R" : "B");
    inorder(root->right);
}

// Main function
int main() {
    Node* root = NULL;

    int values[] = {10, 20, 30, 15, 25, 5, 1};
    int n = sizeof(values)/sizeof(values[0]);

    for (int i = 0; i < n; i++) {
        root = insert(root, values[i]);
        printf("After inserting %d: ", values[i]);
        inorder(root);
        printf("\n");
    }

    printf("\nFinal Red-Black Tree (Inorder Traversal): ");
    inorder(root);
    printf("\n");

    return 0;
}