def Bubblesort(arr):
    size = len(arr)
    for step in range(size - 1):
        for i in range(size - step - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def printArray(arr):
    for num in arr:
        print(num, end=" ")
    print()

print("Enter the number of elements in the list:")
n = int(input())
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

print("Unsorted Array:")
printArray(arr)

Bubblesort(arr)
print("Sorted Array:")
printArray(arr)
