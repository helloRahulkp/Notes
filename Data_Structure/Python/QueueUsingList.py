class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q.pop(0)  

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q[0]

    def is_empty(self):
        return len(self.q) == 0

    def size(self):
        return len(self.q)
    
    def display(self):
        print(self.q)

Q = Queue()
Q.enqueue(
    {
        'company':'HDFC',
        'time':'April 24 11:45 AM',
        'price' : 350
    }
)
Q.enqueue(
    {
        'company':'HDFC',
        'time':'April 24 11:47 AM',
        'price' : 351
    }
)
Q.enqueue(
    {
        'company':'HDFC',
        'time':'April 24 11:48 AM',
        'price' : 358
    }
)
Q.enqueue(
    {
        'company':'HDFC',
        'time':'April 24 11:50 AM',
        'price' : 370
    }
)
Q.display()
check = Q.is_empty()
print(check)
size = Q.size()
print(size)
print(Q.dequeue())
Q.display()

