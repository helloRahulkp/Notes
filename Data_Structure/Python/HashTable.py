class  hastable:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def getHash(self,key):
        len_key=len(key)
        return len_key%self.MAX
    
    def add(self,key,value):
        hash=self.getHash(key)
        self.arr[hash]=value

    def get(self,key):
        hash=self.getHash(key)
        return self.arr[hash]
    
    def delet(self,key):
        hash=self.getHash(key)
        self.arr[hash]=None

    def length(self):
        count=1
        for i in self.arr:
            if i is not None:
                count+=1
        return count
    
    def search(self,key):
        hash=self.getHash(key)
        if self.arr[hash] is not None:
            return True
        else:
            return False

table = hastable()
table.add("name","John")
table.add("age",25)
table.add("city","New York")
print(table.length())
table.add("name","Doe")
print(table.length())
print(table.get("name"))