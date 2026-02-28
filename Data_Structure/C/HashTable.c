#include <stdio.h>
#define SIZE 100

int hashTable[SIZE];

void initHashTable() {
    for (int i = 0; i < SIZE; i++) {
        hashTable[i] = -1; 
    }
}
int getHash(int key){
    return key % SIZE;
}
void add(int key){
    int index = getHash(key);
    if(index < 0 || index >= SIZE) {
        printf("Invalid index\n");
        return;
    }if(hashTable[index] == -1) {
        hashTable[index] = key;
    } else {
        printf("Collision occurred at index %d\n", index);
    }
}
void get(int key){
    int index = getHash(key);
    if(index < 0 || index >= SIZE) {
        printf("Invalid index\n");
        return;
    }if(hashTable[index] != -1) {
        printf("Key %d found at index %d\n", key, index);
    } else {
        printf("Key %d not found\n", key);
    }
}
void delete(int key){
    int index = getHash(key);
    if(index < 0 || index >= SIZE){
        printf("Invalid index\n");
    }if(hashTable[index]!= -1){
        hashTable[index] = -1;
        printf("Key %d deleted from index %d\n", key, index);
    }else {
        printf("Key %d not found\n", key);
    }
}
void printHashTable() {
    for (int i = 0; i < SIZE; i++) {
        if (hashTable[i] != -1) {
            printf("Index %d: %d\n", i, hashTable[i]);
        }
    }
}
int main() {
    initHashTable();
    add(10);
    add(20);
    add(30);
    printHashTable();
    get(20);
    delete(20);
    get(20);
    printHashTable();
    add(10);
    return 0;
}