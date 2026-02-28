#include <stdio.h>
#include <stdlib.h>

// Define structure for a binary tree node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Build tree interactively
struct Node* buildTree() {
    int value;
    struct Node* root = NULL;

    printf("Enter node value (-1 to stop): ");
    scanf("%d", &value);

    if (value == -1) return NULL;

    root = createNode(value);

    printf("Left child of %d\n", value);
    root->left = buildTree();

    printf("Right child of %d\n", value);
    root->right = buildTree();

    return root;
}

// Tree traversals
void preorder(struct Node* root) {
    if (!root) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

void inorder(struct Node* root) {
    if (!root) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

void postorder(struct Node* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    printf("%d ", root->data);
}

// Height and width functions
int height(struct Node* root) {
    if (!root) return 0;
    int lh = height(root->left);
    int rh = height(root->right);
    return (lh > rh ? lh : rh) + 1;
}

int getWidth(struct Node* root, int level) {
    if (!root) return 0;
    if (level == 1) return 1;
    return getWidth(root->left, level - 1) + getWidth(root->right, level - 1);
}

int getMaxWidth(struct Node* root) {
    int maxWidth = 0;
    int h = height(root);
    for (int i = 1; i <= h; i++) {
        int width = getWidth(root, i);
        if (width > maxWidth) maxWidth = width;
    }
    return maxWidth;
}

int main() {
    struct Node* root = buildTree();

    printf("Preorder: ");
    preorder(root);
    printf("\nInorder: ");
    inorder(root);
    printf("\nPostorder: ");
    postorder(root);

    printf("\n\nMaximum Width of Tree: %d\n", getMaxWidth(root));
    return 0;
}