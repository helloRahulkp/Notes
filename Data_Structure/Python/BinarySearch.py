def Bsarch(arr, target):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("Enter the number of elemets in the array: ")
count = int(input())

array = []
print("Enter ",count, "in sorted order: \n")
for i in range(count):
    print("Enter element", i + 1, ":")
    array.append(int(input()))

index = Bsarch(array, int(input("Enter the element to search: ")))

if index == -1:
    print("No elemment found in array")
else :
    print("Element found at index:", index)
