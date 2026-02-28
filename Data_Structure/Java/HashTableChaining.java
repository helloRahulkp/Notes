import java.util.LinkedList;

class hashtable<K,V>{
    private static class HashNode<K, V> {
        K key;
        V value;
        HashNode<K, V> next;

        public HashNode(K key, V value) {
            this.key = key;
            this.value = value;
            this.next = null;
        }
    }

    private LinkedList<HashNode<K, V>>[] buckets;
    private int capasity;
    private int size;

    public hashtable(int capasity){
        this.capasity = capasity;
        this.buckets = new LinkedList[capasity];
        for (int i = 0; i < capasity; i++) {
            buckets[i] = new LinkedList<>();
        }
    }

    private int getHash(K key) {
        int length = key.toString().length();
        return length % capasity;
    }

    public void put(K key,  V value){
        int index = getHash(key);
        LinkedList<HashNode<K, V>> bucket = buckets[index];
        for (HashNode<K, V> node : bucket) {
            if (node.key.equals(key)) {
                node.value = value; 
                return;
            }
        }
        
        HashNode<K, V> newNode = new HashNode<>(key, value);
        bucket.add(newNode);
        size++;
    }

    public V get(K key){
        int index = getHash(key);
        LinkedList<HashNode<K, V>> bucket = buckets[index];
        for (HashNode<K, V> node : bucket) {
            if (node.key.equals(key)) {
                return node.value;
            }
        }
        return null; 
    }

    public void remove(K key){
        int index = getHash(key);
        LinkedList<HashNode<K, V>> bucket = buckets[index];
        for (HashNode<K,V > node : bucket) {
            if (node.key.equals(key)){
                bucket.remove(node);
                size--;
                return;
            }
        }
    }

    public void display(){
        for (int i = 0; i < capasity; i++) {
            LinkedList<HashNode<K,V>> bucket = buckets[i];
            System.out.print("Bucket " + i + ": ");
            for (HashNode<K,V> node : bucket) {
                System.out.print("[" + node.key + " : " + node.value + "] ");
            }
            System.out.println();
        }
    }

}

public class HashTableChaining {
    public static void main(String[] args) {
        hashtable<String, Integer> hashtable = new hashtable<>(10);
        hashtable.put("name", 1);
        hashtable.put("age", 2);
        hashtable.put("address", 3);
        hashtable.put("phone", 4);
        hashtable.put("email", 5);

        System.out.println("Value for key 'name': " + hashtable.get("name"));
        System.out.println("Value for key 'age': " + hashtable.get("age"));
        System.out.println("Value for key 'address': " + hashtable.get("address"));
        System.out.println("Value for key 'phone': " + hashtable.get("phone"));
        System.out.println("Value for key 'email': " + hashtable.get("email"));
        hashtable.remove("age");
        hashtable.display();
        System.err.println("new hash table");
        hashtable<String, String> hashtable2 = new hashtable<>(5);
        hashtable2.put("name", "John Doe");
        hashtable2.put("age", "30");
        hashtable2.put("address", "123 Main St");
        hashtable2.put("phone", "555-1234");
        hashtable2.put("city","New York");
        hashtable2.display();
    }
}
