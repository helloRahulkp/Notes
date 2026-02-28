class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None for i in range(size)]
        self.values = [None for i in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for i in range(self.size):  
            if self.keys[index] is None:
                self.keys[index] = key
                self.values[index] = value
                return
            elif self.keys[index] == key:
                
                if isinstance(self.values[index], list):
                    self.values[index].append(value)
                else:
                    self.values[index] = [self.values[index], value]
                return
            index = (index + 1) % self.size
        print("Hash table is full.")

    def get(self, key):
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.keys[index] is None:
                return None
            elif self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for _ in range(self.size):
            if self.keys[index] is None:
                return  
            elif self.keys[index] == key:
                if isinstance(self.values[index], list):
                    
                    self.values[index] = self.values[index][1:]
                    if len(self.values[index]) == 1:
                        self.values[index] = self.values[index][0]
                else:
                    self.keys[index] = None
                    self.values[index] = None
                return
            index = (index + 1) % self.size

table = HashTable(10)
table.insert(1, "John")
table.insert(1, "Doe")
table.insert(2, "Jane")
table.insert(3, "Smith")
table.insert(3, "Alice")
table.insert(3, "Bob")

print("Get key 1:", table.get(1))
print("Get key 3:", table.get(3))
print("Keys ", table.keys)
print("Values ", table.values)