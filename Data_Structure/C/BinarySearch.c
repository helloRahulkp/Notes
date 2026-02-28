#include<stdio.h>

int BinarySearch(int arr[],int size, int target){
    int left = 0;
    int right = size-1;

    while(left <= right){
        int mid = left + (right-left)/2;

        if(arr[mid]==target){
            return mid;
        }else if(arr[mid]< target){
            left = mid + 1;
        }else{
            right = mid -1;
        }
    }
    return -1;
}

int main(){

    printf("enter the size of the array: ");
    int count;
    scanf("%d",&count);
    int array[count];
    printf("Enter the %d number of elements in sorted order\n",count);
    for(int i =0;i<count;i++){
        printf("Element %d : ",i+1);
        scanf("%d",&array[i]);
    }

    printf("Enter target to search:");
    int value;
    scanf("%d",&value);

    int index = BinarySearch(array,count,value);

    if(index == -1){
        printf("No element found");
    }else{
        printf("Element found at %d", index);
    }
    return 0;
}