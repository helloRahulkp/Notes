class Node{
    String key;
    Object value;
    Node next;
    Node prev;
    public Node(String key, Object value){
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}
public class LinkedHashMap {
    public static final int SIZE = 10;
    private Node[] table;
    private Node head;
    private Node tail;

    public LinkedHashMap() {
        this.table = new Node[SIZE];
        for (int i = 0; i < SIZE; i++) {
            table[i] = null;
        }
        this.head = null;
        this.tail = null;
    }
    private int getHash(String key){
        return key.length() % SIZE;
    }
    public void add(String key, Object value){
        int index =getHash(key);
        Node newNode = new Node(key, value);
        if(table[index]==null){
            table[index] = newNode;
            if(head == null){
                head = newNode;
                tail = newNode;
            }else{
                tail.next = newNode;
                newNode.prev =tail;
                tail = newNode;
            }
        }else{
            System.out.println("Collision detected at index"+ index);
        }
    }
    public Object getvalue(String key){
        int index = getHash(key);
        Node current = table[index];
        while(current !=null){
            if(current.key.equals(key)){
                return current.value;
            }
            current = current.next;
        }
        System.out.println("No value found for "+ key);
        return null;
    }
    public void delete(String key){
        int index = getHash(key);
        Node current = table[index];
        while(current != null){
            if(current.key.equals(key)){
                if(current.prev !=null){
                    current.prev.next = current.next;
                }else{
                    table[index] = current.next;
                }
                if(current.next != null){
                    current.next.prev = current.prev;
                }else{
                    tail = current.prev;
                }
                return;
            }
            current = current.next;
        }
        System.out.println("No value found for "+ key);
    }
    public boolean search(String key) {
        int index = getHash(key);
        Node current = table[index];
        while (current != null) {
            if (current.key.equals(key)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
    public void printAll(){
        Node current = head;
        while(current != null){
            System.out.println("Key: " + current.key + ", Value: " + current.value);
            current = current.next;
        }
    }
    public static void main(String[] args) {
        LinkedHashMap lhm = new LinkedHashMap();
        System.out.println("LinkedHashMap class is created");
        lhm.add("name", "John Doe");
        lhm.add("age", 30);
        lhm.add("city", "New York");
        lhm.printAll();
        System.out.println("Search for name: " + lhm.search("name"));
        System.out.println("Value for key 'name': " + lhm.getvalue("name"));
        lhm.delete("age");
        lhm.printAll();
    }
}