class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBegining(self, data):
        node =Node(data,self.head)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node
    def insertMultipleValues(self,data_list):
        for data in data_list:
            self.insertAtBegining(data)
    def traverse(self):
        if self.head is None:
            print("The linked list is empty")
            return
        itr = self.head
        linkedListStr = ""
        while itr:
            linkedListStr += str(itr.data) + "-->"
            itr = itr.next
        print(linkedListStr)

    def reverse(self):
        if self.head is None:
            print("The linked list is empty")
            return
        prev = None
        current = self.head
        while current is not None:
            next = current.next #or alternative next = next.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        

ll=LinkedList()
ll.insertAtBegining(1)
list = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
ll.insertMultipleValues(list)
ll.traverse()
ll.reverse()
ll.traverse()