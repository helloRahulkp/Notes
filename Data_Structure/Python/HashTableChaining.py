class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  

    def _hash(self, key):
        length = len(key)
        return length % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
    
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value)) 
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return "Key not found"

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        return "Key not found"

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

if __name__ == "__main__":
    ht = HashTable()  
    ht.insert("name", "John")
    ht.insert("age", 25)
    ht.insert("city", "New York")
    ht.insert("name", "Doe")
    ht.display()
    print(ht.get("name"))
    print(ht.get("age"))
    ht.delete("name")
    ht.display()