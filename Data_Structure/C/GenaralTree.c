#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int data;
    int childCount;
    struct Node** children;
}Node;

//Create a new node

Node* createNode(int data,int childCount){
    Node* node = (Node*)malloc(sizeof(Node));
    node->data = data;
    node->childCount = childCount;
    node->children = (Node**)malloc(childCount * sizeof(Node*));
    return node;
}

// Print tree (preorder)

void printTree(Node* root){
    if(root == NULL) return;
    printf("%d ", root->data);
    for(int i = 0; i< root->childCount; i++){
        printTree(root->children[i]);
    }
}

int main(){
    Node* root = createNode(1,3);
    root->children[0] = createNode(2, 0);
    root->children[1] = createNode(3, 2);
    root->children[1]->children[0] = createNode(4, 0);
    root->children[1]->children[1] = createNode(5, 0);
    root->children[2] = createNode(6, 0);

    printf("General Tree Preorder: ");
    printTree(root);
    return 0;
}