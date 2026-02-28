#include<stdio.h>
#define SIZE 10
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
    }
    while (hashTable[index] != -1){
        printf("Collision occurred at index %d\n", index);
        index = (index + 1) % SIZE;

    }
    hashTable[index] = key;
    printf("Key %d added at index %d\n", key, index);
}

void get(int key){
    int index = getHash(key);
    if(index < 0 || index >= SIZE) {
        printf("Invalid index\n");
        return;
    }
    while (hashTable[index] != -1){
        if(hashTable[index] == key){
            printf("Key %d found at index %d\n", key, index);
            return;
        }
        index = (index + 1) % SIZE;
    }
    printf("Key %d not found\n", key);
}
void delete(int key){
    int index = getHash(key);
    if(index < 0 || index >= SIZE){
        printf("Invalid index\n");
        return;
    }
    while (hashTable[index] != -1){
        if(hashTable[index] == key){
            hashTable[index] = -1;
            printf("Key %d deleted from index %d\n", key, index);
            return;
        }
        index = (index + 1) % SIZE;
    }
    printf("Key %d not found\n", key);
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
    printf("\n");
    get(20);
    delete(20);
    get(20);
}