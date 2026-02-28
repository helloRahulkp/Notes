public class HashTableLinearProbing {
    private static final int SIZE = 10;
    private String[] keys;
    private Object[] values;

    public HashTableLinearProbing() {
        this.keys = new String[SIZE];
        this.values = new Object[SIZE];
    }

    private int getHash(String key) {
        return Math.abs(key.hashCode() % SIZE);
    }

    public void add(String key, Object value) {
        int index = getHash(key);
        while (keys[index] != null) {
            if (keys[index].equals(key)) {
                values[index] = value; // Update existing key
                return;
            }
            System.out.println("Collision detected at index " + index + " for key " + key);
            index = (index + 1) % SIZE;
        }
        keys[index] = key;
        values[index] = value;
    }

    public Object get(String key) {
        int index = getHash(key);
        while (keys[index] != null) {
            if (keys[index].equals(key)) {
                return values[index];
            }
            index = (index + 1) % SIZE;
        }
        return null;
    }

    public void delete(String key) {
        int index = getHash(key);
        while (keys[index] != null) {
            if (keys[index].equals(key)) {
                keys[index] = null;
                values[index] = null;
                return;
            }
            index = (index + 1) % SIZE;
        }
    }

    public void display() {
        for (int i = 0; i < SIZE; i++) {
            if (keys[i] != null) {
                System.out.println("Index " + i + ": Key=" + keys[i] + ", Value=" + values[i]);
            } else {
                System.out.println("Index " + i + ": Empty");
            }
        }
    }

    public static void main(String[] args) {
        HashTableLinearProbing ht = new HashTableLinearProbing();
        ht.add("FB", "value1");   
        ht.add("Ea", "value2");   
        ht.add("a", "value3");    
        ht.add("k", "value4");    
        ht.add("apple", "value5");
        ht.add("b", "value6");    
    
        ht.display();
    }
}
