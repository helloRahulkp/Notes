from collections import deque

Q = deque()
Q.appendleft(
    {
        'company':'HDFC',
        'time':'April 24 11:45 AM',
        'price' : 350
    }
)
Q.appendleft(
     {
        'company':'HDFC',
        'time':'April 24 11:47 AM',
        'price' : 351
    }
)
Q.appendleft(
    {
        'company':'HDFC',
        'time':'April 24 11:48 AM',
        'price' : 358
    }
)
Q.appendleft(
     {
        'company':'HDFC',
        'time':'April 24 11:50 AM',
        'price' : 370
    }
)
print(Q)
print("Queue Deque: ", Q)
print("Queue Deque Length: ", len(Q))
print("Queue Deque First Element: ", Q[0])
print("Queue Deque Last Element: ", Q[-1])
print("Queue Deque Second Element: ", Q[1])
print("Queue deque: ", Q.pop())
print("Queue Deque After deque: ", Q)
print("Queue Deque Length After deque: ", len(Q))
print("Queue Deque First Element After deque: ", Q[0])
print("Queue Deque Last Element After deque: ", Q[-1])
print("Queue Deque Second Element After deque: ", Q[1])
