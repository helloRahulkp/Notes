class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insertAtBegining(self, data):
        node = Node(data,self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
    def forwardTraversal(self):
        if self.head is None:
            print("The list is empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end="<->")
            itr = itr.next
        print()
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(data, None)
        itr.next.prev = itr
    def insertListValueAtEnd(self, data_list):
        for data in data_list:
            self.insertAtEnd(data)
    def insertListValueAtBegining(self, data_list):
        for data in data_list:
            self.insertAtBegining(data)
    def lenOfList(self):
        counter = 0
        itr=self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter
    def removeAtIndex(self, index):
        if index < 0 or index >= self.lenOfList():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        counter = 0
        itr = self.head
        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                if itr.next is not None:
                    itr.next.prev = itr
                break
            itr = itr.next
            counter += 1
    def insertAtIndex(self, index, data):
        if index < 0 or index > self.lenOfList():
            raise Exception("Invalid Index")
        if index == 0:
            self.insertAtBegining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node =Node(data,itr.next,itr)
                itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1
    def insertAfterValue(self, value, data):
        if self.head is None:
            raise Exception("The list is empty")
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next, itr)
                if itr.next is not None:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
    def removeByValue(self, value):
        if self.head is None:
            raise Exception("The list is empty")
        itr = self.head
        while itr:
            if itr.data == value:
                if itr.prev is not None:
                    itr.prev.next = itr.next
                if itr.next is not None:
                    itr.next.prev = itr.prev
                if itr == self.head:
                    self.head = itr.next
                break
            itr = itr.next  
    def backwardTraversal(self):
        if self.head is None:
            print("The list is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        while itr:
            print(itr.data, end="<->")
            itr = itr.prev
        print()

dl = DoublyLinkedList()
dl.insertAtBegining(10)
dl.insertAtBegining(20)
dl.insertAtBegining(30)
dl.forwardTraversal()
dl.insertListValueAtEnd(["Apple", "Banana", "Mango","Orange"])
dl.forwardTraversal()
dl.insertListValueAtBegining(["Grapes", "Pineapple", "Watermelon"])
dl.forwardTraversal()
print("Length of the list is: ", dl.lenOfList())
dl.forwardTraversal()
dl.removeAtIndex(0)
dl.forwardTraversal()
dl.removeAtIndex(4)
dl.forwardTraversal()
dl.insertAtIndex(0, "First")
dl.insertAtIndex(2, "Middle")
dl.insertAtIndex(5, "Last")
dl.forwardTraversal()
dl.insertAfterValue("First", "After Apple")
dl.insertAfterValue(data = "Second", value="First")
dl.forwardTraversal()
dl.removeByValue(30)
dl.forwardTraversal()
dl.backwardTraversal()