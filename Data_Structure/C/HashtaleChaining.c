#include <stdio.h>
#include <stdlib.h>

typedef struct KeyValuePair {
    int key;
    int value;
    struct KeyValuePair* next;
} KeyValuePair;


typedef struct HashTable {
    int size;
    KeyValuePair** table; 
} HashTable;

int hashFunction(int key, int size) {
    return key % size;
}

KeyValuePair* createKeyValuePair(int key, int value) {
    KeyValuePair* newPair = (KeyValuePair*)malloc(sizeof(KeyValuePair));
    if (newPair != NULL) {
        newPair->key = key;
        newPair->value = value;
        newPair->next = NULL;
    }
    return newPair;
}

HashTable* createHashTable(int size) {
    HashTable* newTable = (HashTable*)malloc(sizeof(HashTable));
    if (newTable != NULL) {
        newTable->size = size;
        newTable->table = (KeyValuePair**)calloc(size, sizeof(KeyValuePair*));
    }
    return newTable;
}

void insertChaining(HashTable* hashTable, int key, int value) {
    int index = hashFunction(key, hashTable->size);
    KeyValuePair* newPair = createKeyValuePair(key, value);

    newPair->next = hashTable->table[index];
    hashTable->table[index] = newPair;
}

int retrieveChaining(HashTable* hashTable, int key) {
    int index = hashFunction(key, hashTable->size);
    KeyValuePair* current = hashTable->table[index];

    while (current != NULL) {
        if (current->key == key) {
            return current->value; 
        }
        current = current->next;
    }
    return -1; 
}

void removeChaining(HashTable* hashTable, int key) {
    int index = hashFunction(key, hashTable->size);
    KeyValuePair* current = hashTable->table[index];
    KeyValuePair* previous = NULL;
    while (current != NULL) {
        if (current->key == key) {
            if (previous == NULL) {
                hashTable->table[index] = current->next;
            } else {
                previous->next = current->next;
            }
            free(current);
            return;
        }
        previous = current;
        current = current->next;
    }
}

void displayHashTable(HashTable* hashTable) {
    for (int i = 0; i < hashTable->size; i++) {
        printf("Bucket %d: ", i);
        KeyValuePair* current = hashTable->table[i];
        while (current != NULL) {
            printf("[%d -> %d] ", current->key, current->value);
            current = current->next;
        }
        printf("\n");
    }
}

void freeHashTable(HashTable* hashTable) {
    for (int i = 0; i < hashTable->size; i++) {
        KeyValuePair* current = hashTable->table[i];
        while (current != NULL) {
            KeyValuePair* temp = current;
            current = current->next;
            free(temp);
        }
    }
    free(hashTable->table);
    free(hashTable);
}

int main() {
    HashTable* hashTable = createHashTable(10); 

    insertChaining(hashTable, 10, 100);
    insertChaining(hashTable, 15, 150);
    insertChaining(hashTable, 20, 200);
    insertChaining(hashTable, 25, 250);
    insertChaining(hashTable, 30, 300);
    insertChaining(hashTable, 35, 350);
    insertChaining(hashTable, 40, 400);
    insertChaining(hashTable, 45, 450);
    insertChaining(hashTable, 12, 120);
    printf("Hash Table Contents:\n");
    displayHashTable(hashTable);
    printf("\nValue for 10: %d\n", retrieveChaining(hashTable, 10));
    printf("\nRemoving key 15\n");
    removeChaining(hashTable, 15);
    printf("Hash Table Contents after removal:\n");
    displayHashTable(hashTable);
    freeHashTable(hashTable);
    
    return 0;
}
