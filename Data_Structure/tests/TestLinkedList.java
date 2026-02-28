import org.junit.Test;
import static org.junit.Assert.*;

public class TestLinkedList {
    @Test
    public void testAppend() {
        LinkedList ll = new LinkedList();
        ll.append(1);
        ll.append(2);
        assertEquals(1, ll.head.value);
        assertEquals(2, ll.head.next.value);
    }
}
