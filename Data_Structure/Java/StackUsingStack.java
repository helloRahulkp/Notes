import java.util.*;
public class StackUsingStack {
    public static void main(String[] args) {
        System.out.println("Stack using Stack");
        Stack<String> stack = new Stack<>();
        stack.push("1");
        stack.push("2");
        stack.push("3");
        stack.push("Hello");
        stack.push("World");;
        System.out.println("Stack: " + stack);
        System.out.println("Length of stack: " + stack.size());
        System.out.println("Top element of stack: " + stack.peek());
        System.out.println("Popped element: " + stack.pop());
        System.out.println("Stack after pop: " + stack);
        System.out.println("Length of stack: " + stack.size());
        System.out.println("Top element of stack: " + stack.peek());
        System.out.println("Popped element: " + stack.pop());
    }
}
