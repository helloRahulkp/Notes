class Node {
    String data;
    Node next;

    public Node(String data) {
        this.data = data;
        this.next = null;
    }
}

class Linkedlist {

    private Node head;
    Linkedlist() {
        this.head = null;
    }

    public void insertAtBeginning(String data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }
    public void insertAtEnd(String data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }

    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }

    public void insertMultipleAtBeginning(String[] data) {
        for (String value : data) {
            insertAtBeginning(value);
        }
    }
    public void insertMultipleAtEnd(String[] data) {
        for (String value : data) {
            insertAtEnd(value);
        }
    }

    public int length() {
        int count = 0;
        Node current = head;
        while (current != null) {
            count++;
            current = current.next;
        }
        return count;
    }

    public void insertAtIndex(int index, String data) {
        if (index < 0 || index > length()) {
            System.out.println("Index out of bounds");
            return;
        }
        if (index == 0) {
            insertAtBeginning(data);
            return;
        }
        Node newNode = new Node(data);
        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        newNode.next = current.next;
        current.next = newNode;
    }

    public void removeAtIndex(int index) {
        if (index < 0 || index >= length()) {
            System.out.println("Index out of bounds");
            return;
        }
        if (index == 0) {
            head = head.next;
            return;
        }
        Node current = head;
        for (int i = 0; i < index - 1; i++) {
            current = current.next;
        }
        current.next = current.next.next;
    }

    public void insertAfterValue(String target, String data) {
        Node current = head;
        while (current != null && !current.data.equals(target)) {
            current = current.next;
        }
        if (current == null) {
            System.out.println("Value not found");
            return;
        }
        Node newNode = new Node(data);
        newNode.next = current.next;
        current.next = newNode;
    }
    public void removeByValue(String value) {
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        if (head.data.equals(value)) {
            head = head.next;
            return;
        }
        Node current = head;
        while (current.next != null && !current.next.data.equals(value)) {
            current = current.next;
        }
        if (current.next == null) {
            System.out.println("Value not found");
            return;
        }
        current.next = current.next.next;
    }
    public void clear() {
        head = null;
    }
}

public class LinkedList {
    public static void main(String[] args) {
        Linkedlist list = new Linkedlist();
        list.insertAtBeginning("Apple");
        list.insertAtEnd("Banana");
        list.insertAtEnd("Orenge");
        list.display(); 

    
        String [] fruits = {"Pineapple", "Mango", "Grapes"};
        list.insertMultipleAtBeginning(fruits);
        list.display();

        // list.insertMultipleAtBeginning(new String[]{"Jackfruite", "Mango"});
        // list.display(); 

        list.insertMultipleAtEnd(new String[]{"Givi", "Pineapple"});
        list.display(); 

        System.out.println("Length: " + list.length()); 

        list.insertAtIndex(3, "Grapes");
        list.display(); 

        list.removeAtIndex(2);
        list.display(); 

        list.insertAfterValue("Pineapple", "Papaya");
        list.display(); 

        list.removeByValue("Grapes");
        list.display(); 
    }

    public void add(int i) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'add'");
    }
    
}
