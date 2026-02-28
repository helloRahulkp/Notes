class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def insertAtBegining(self,data):
        node = Node(data,self.head)
        self.head=node
    def insertAtEnd(self,data):
        if self.head is None:
            self.head =Node(data,None)
            return
        itr =self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def print(self):
        if self.head is None:
            print("The linked list is empty")
            return
        
        itr=self.head
        linkedlist_str=""
        while itr:
            linkedlist_str+=str(itr.data)+"-->"
            itr=itr.next
        print(linkedlist_str)
    def inserListValue(self,data_list):
        for  data in data_list:
            self.insertAtEnd(data)
    def lenOfLinkedList(self):
        counter =0
        itr =self.head
        if itr is None:
            print("The list is empty")
            return
        while itr:
            counter+=1
            itr=itr.next
        return counter
    def removeAtIndex(self,index):
        if index<0 or index>self.lenOfLinkedList():
            raise Exception("Invalid Index")
        if index ==0:
            self.head=self.head.next
            return
        counter=0
        itr=self.head
        while itr:
            if counter == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            counter+=1
    def insertAtIndex(self, index, data):
        if index < 0 or index > self.lenOfLinkedList():
            raise Exception("Invalid Index")

        if index == 0: 
            self.insertAtBegining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  
                node = Node(data, itr.next)  
                itr.next = node 
                break       
            itr = itr.next
            count += 1
    def insertAfterValue(self,value,data):
        itr = self.head
        while itr:
            if itr.data is value:
                node = Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
    def removeByValue(self,value):
        itr=self.head
        while itr:
            if itr.next.data is value:
                itr.next=itr.next.next
                break

ll=LinkedList()
list=["Apple","Banan","Mango","Orenge"]
ll.inserListValue(list)
ll.print()
ll.removeAtIndex(2)
ll.print()
ll.insertAtIndex(1,"Givi")
ll.print()
ll.insertAtIndex(3,"jackfruit")
ll.print()
ll.insertAfterValue("Apple",10)
ll.print()
ll.removeByValue(10)
ll.print()
print("Length of linked list:",ll.lenOfLinkedList())
        