
import java.util.LinkedList;
import java.util.Queue;


public class QueueUsingDeque {
    public static void main(String[] args) {
        Queue <String> stockQueue = new LinkedList<>();
        stockQueue.add("AAPL");   
        stockQueue.add("GOOGL");  
        stockQueue.add("MSFT");   
        stockQueue.add("AMZN");   
        stockQueue.add("TSLA");   
        stockQueue.add("NFLX");   
        stockQueue.add("FB");     
        stockQueue.add("BABA");   
        stockQueue.add("TCS");    
        stockQueue.add("INFY");   

        System.out.println("Stock Queue: " + stockQueue);

        String removedStock = stockQueue.remove();
        System.out.println("Removed stock: " + removedStock);

        System.out.println("Stock Queue after removal: " + stockQueue);
    }
}