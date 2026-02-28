#include <stdio.h>
#include <stdlib.h>
struct Node {
    int data;
    struct Node* next;
};

struct Node* insert(struct Node* head,int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if(head == NULL){
        newNode->data = data;
        newNode->next = NULL;
        return newNode;
    }
    struct Node* temp = head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    newNode->data = data;
    newNode->next = NULL;
    temp->next = newNode;
    return head;
}
struct Node* insertMultiple(struct Node* head,int data[], int size){
    for(int i =0;i<size;i++){
        head = insert(head, data[i]);
    }
    return head;
}
struct Node* reverse(struct Node* head){
    struct Node* prev,* current, * next;
    prev = NULL;
    current = head;
    next = NULL;
    while(current != NULL){
        next = current->next;
        current->next = prev;
        prev =current;
        current = next;
    }
    head = prev;
    return head;
}
void printList(struct Node* head){
    struct Node* temp = head;
    while(temp != NULL){
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
int main(){
    struct Node* head = NULL;
    head = insert(head, 1);
    head = insert(head, 2);
    head = insert(head, 3);
    head = insert(head, 4);
    head = insert(head, 5);
    int data[] = {6, 7, 8, 9, 10};
    head = insertMultiple(head, data, 5);
    printf("Original List: ");
    printList(head);
    printf("Reversed List: ");
    head = reverse(head);
    printList(head);
    return 0;
}

