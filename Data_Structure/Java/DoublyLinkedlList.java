class DoublyLinkedlist {

    class Node {
        String data;
        Node previous;
        Node next;

        public Node(String data) {
            this.data = data;
        }
    }
    Node head, tail = null;
    public void insertAtEnd(String data) {
        
        Node newNode = new Node(data);
        if (head == null) {
            head = tail = newNode;
            head.previous = null; 
            tail.next = null;     
        } else {
            
            tail.next = newNode;
            newNode.previous = tail;
            tail = newNode;
            tail.next = null;     
        }
    }
    public void insertMultipleAtEnd(String[] data) {
        for (String value : data) {
            insertAtEnd(value);
        }
    }
    public void insertMultipleAtBeginning(String[] data){
        for(String value : data){
            insertAtBeginning(value);
        }
    }
    public void insertAtBeginning(String data){
        Node newNode = new Node(data);
        if(head == null){
            head = tail = newNode;
            head.previous =null;
            tail.next = null;
        }else{
            newNode.next = head;
            head.previous =newNode;
            head = newNode;
        }
    }
    public void insertAtIndex(int index, String data){
        if(index <0 ||index > lengthOfList()){
            System.out.print("Index out of bounds");
            return;
        }
        if(index == 0){
            insertAtBeginning(data);
            return;
        }else if(index == lengthOfList()){
            insertAtEnd(data);
            return;
        }else{
            Node newNode = new Node(data);
            Node current = head;
            for(int i =0;i<index-1;i++){
                current = current.next;
            }
            newNode.next = current.next;
            current.next.previous = newNode;
            current.next = newNode;
            newNode.previous = current; 
        }
    }
    public void forwardTraversal() {
        if (head == null) {
            System.out.println("The list is empty");
            return;
        }
        Node current = head;
        System.out.print("Forward Traversal: ");
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
    public void backwardTraversal() {
        if (tail == null) {
            System.out.println("The list is empty");
            return;
        }
        Node current = tail;
        System.out.print("Backward Traversal: ");
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.previous;
        }
        System.out.println();
    }
    public int lengthOfList(){
        int count =0;
        Node current = head;
        while(current != null){
            count++;
            current = current.next;
        }
        return count;
    }
    public void removeByValue(String value) {
        if (head == null) {
            System.out.println("The list is empty");
            return;
        }

        Node current = head;

        while (current != null) {
            if (current.data == value) {
                
                if (current == head) {
                    head = head.next;
                    if (head != null) { 
                        head.previous = null; 
                    }
                } 
                
                else if (current == tail) {
                    tail = tail.previous;
                    if (tail != null) { 
                        tail.next = null; 
                    }
                } 
                
                else {
                    current.previous.next = current.next;
                    current.next.previous = current.previous;
                }
                System.out.println("Removed: " + value);
                return;
            }
            current = current.next;
        }
        
        System.out.println("Value not found: " + value);
    }
    public void removeByIndex(int index){
        if(head == null){
            System.out.print("The list is empty");
            return;
        }
        if(index < 0 || index >= lengthOfList()){
            System.out.print("Index out of bounds\n");
            return;
        }
        if(index == 0){
            head =  head.next;
            head.previous = null;
        }else if(index == lengthOfList()-1){
            tail = tail.previous;
            tail.next = null;
        }else{
            Node current = head;
            for(int i = 0; i < index; i++){
                current = current.next;
            }
            current.previous.next = current.next;
            current.next.previous = current.previous;
        }

    }
}
public class DoublyLinkedlList{
    public static void main(String[] args) {
        DoublyLinkedlist dll = new DoublyLinkedlist();
        dll.insertAtEnd("10");
        dll.insertAtEnd("20");
        dll.insertAtEnd("30");
        dll.insertAtBeginning("40");
        dll.forwardTraversal();
        dll.backwardTraversal();
System.out.println("Length of the list: " + dll.lengthOfList());
        dll.removeByIndex(0);
        dll.forwardTraversal();
        dll.insertMultipleAtBeginning(new String[]{"Apple", "Banana", "Cherry"});
        dll.forwardTraversal();
        dll.insertAtIndex(1,"Orange");
        dll.forwardTraversal();
        dll.backwardTraversal();
    }
}
