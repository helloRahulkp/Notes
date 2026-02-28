
import java.util.Scanner;

public class BinarySearch {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of elements: ");
        int count = sc.nextInt();
        int [] arr = new int[count];

        System.err.println("Enter"+ count + "elemets in sorted order:\n");
        for(int i = 0; i< count; i++){
            System.err.println("Element "+i);
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter the element to search: ");
        int value = sc.nextInt();
        int index = BSearch(arr, value);
        if(index != -1){
            System.out.println("Element found at index: " + index);
        }else{
            System.out.println("Element not found in the array.");
        }
    
    }

    public static int BSearch(int array[],int target){
        int left = 0;
        int right = array.length-1;
        while(left <= right){
            int mid = left + (right - left) / 2;

            if(array[mid] == target){
                return mid; // Target found
            }else if(array[mid] < target){
                left = mid + 1; // Search in the right half
            }else{
                right = mid - 1;
            }
        }
        return -1;
    }
    
}
