class NodeR {
    String data;
    NodeR next;

    NodeR(String data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedListR{
    private NodeR head;
    LinkedListR() {
        this.head = null;
    }
    public void insertAtBeginning(String data){
        NodeR newNode = new NodeR(data);
        if (head == null){
            head = new NodeR(data);
            return;
        }else{
            newNode.next= head;
            head = newNode;
        }
    }
    public void insertMultipleValues(String[] data_list){
        for (String value : data_list){
            insertAtBeginning(value);
        }
    }
    public void traverse(){
        NodeR current = head;
        if(current == null){
            System.out.println("List is empty");
            return;
        }
        while(current != null){
            System.out.print(current.data + " -> ");
            current = current.next;
        }
    }
    public void reverseList(){
        NodeR prev = null;
        NodeR current = head;
        NodeR next = null;
        while(current!=null){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }
}

public class LinkedListReverse {
    public static void main(String[] args) {
        LinkedListR list = new LinkedListR();
        list.insertAtBeginning("A");
        list.insertAtBeginning("B");
        list.insertMultipleValues(new String[]{"Apple", "Banana", "Cherry","Date"});
        list.traverse();
        System.out.println("\nReversed List:");
        list.reverseList();
        list.traverse();

    }
}
