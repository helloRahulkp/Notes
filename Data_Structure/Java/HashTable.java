class hashTable{
    private static final int SIZE = 10;
    private Object[] table;
    
    public hashTable() {
        this.table = new Object[SIZE];
        for (var each : table) {
            each = null;
        }
    }
    private int getHash(String key){
        return key.length() % SIZE;
    }
    public void add(String key, Object value){
        int index = getHash(key);
        if (table[index] == null){
            table[index] =value;
        }else{
            System.out.println("Collission detected at index"+ index);
        }
    }
    public Object get(String key){
        int index = getHash(key);
        if(table[index]!=null){
            return table[index];
        }else{
            System.out.println("No value found at index"+ index);
            return null;
        }
    }
    public void delete(String key){
        int index = getHash(key);
        if(table[index]!=null){
            table[index] = null;
        }else{
            System.out.println("No value found at index"+ index);
        }
    }
    public void length(){
        int count = 0;
        for (var each : table) {
            if (each != null) {
                count++;
            }
        }
        System.out.println("Length of the hash table is: " + count);
    }
    public boolean search(String key){
        int index = getHash(key);
        if(table[index]!=null){
            return true;
        }else{
            return false;
        }
    }
}
public class HashTable {
    public static void main(String[] args) {
        hashTable ht = new hashTable();
        System.out.println("HashTable class is created");
        ht.add("name", "John Doe");
        ht.add("age", 30);
        ht.add("city", "New York");
        ht.add("country", "USA");
        ht.add("occupation", "Engineer");
        ht.add("hobby", "Reading");
        ht.add("language", "Java");
        ht.add("food", "Pizza");    
        System.out.println("Added name: " + ht.get("name"));
        System.out.println("Added age: " + ht.get("age"));
        System.out.println("Added city: " + ht.get("city"));
        System.out.println("Added country: " + ht.get("country"));
        System.out.println("Added occupation: " + ht.get("occupation"));
        System.out.println("Added hobby: " + ht.get("hobby"));        
        System.out.println("Added language: " + ht.get("language"));
        System.out.println("Added food: " + ht.get("food"));
        ht.length();
        ht.delete("name");
        ht.delete("age");
        System.out.println("Deleted name: " + ht.get("name"));
        System.out.println("Deleted age: " + ht.get("age"));
        System.err.println("Search for name: " + ht.search("name"));
        System.out.println("Search for country: " + ht.search("country"));
    }
}
