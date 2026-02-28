#include <stdio.h>

void BubleSort(int arr[], int size){
    for (int step = 0; step<size-1;step++){
        for (int i = 0; i<size-step-1;i++){
            if(arr[i]>arr[i+1]){
                int temp = arr[i];
                arr[i]=arr[i+1];
                arr[i+1]=temp;
            }
        }
    }
}


int main(){
    int count;
    printf("Enter the number of elements int the array: ");
    scanf("%d",&count);

    int array[count];

    printf("Enter the %d elemtns to the array\n", count);
    for(int i =0;i<count;i++){
        printf("arr[%d]:",i);
        scanf("%d",&array[i]);
    }

    BubleSort(array,count);
    printf("Sorted Arrya\n");
    for(int i=0;i<count;i++){
        printf("%d ",array[i]);
    }

    return 0;
}