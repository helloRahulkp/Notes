#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 10

typedef struct
{
    int front;
    int rear;
    int arr[MAX];
}QueueUsingArray;

void initQ(QueueUsingArray* q){
    q->front=-1;
    q->rear=-1;
}

bool isFull(QueueUsingArray* q){
    return q->rear == MAX-1;
}

bool isEmpty(QueueUsingArray* q){
    return q->front == -1;
}
void enqueue(QueueUsingArray* q,int value){
    if(isFull(q)){
        printf("Queue is full");
        return;
    }
    if(isEmpty(q)){
        q->front =  0;
        q->rear = 0;
    }else{
        q->rear++;
    }
    q->arr[q->rear]=value;
    printf("Enqueued %d\n", value);
}

int dequeue(QueueUsingArray* q){
    if(isEmpty(q)){
        printf("The queue is empty");
        return-1;
    }
    int value = q->arr[q->front];
    if(q->front  == q->rear){
        q->front = -1;
        q->rear = -1;
    }else{
        q->front++;
    }
    return value;
}

void displayQ(QueueUsingArray* q){
    if(isEmpty(q)){
        printf("The queue is empty");
        return;
    }
    printf("Elements of Queue : ");
    for(int i = q->front;i<=q->rear;i++){
        printf("%d--",q->arr[i]);
    }
    printf("\n");
}

int main(){
    QueueUsingArray q;
    initQ(&q);

    enqueue(&q,10);
    enqueue(&q,20);
    enqueue(&q,30);

    displayQ(&q);

    printf("Dequeued: %d\n", dequeue(&q));
    displayQ(&q);


    return 0;
}
