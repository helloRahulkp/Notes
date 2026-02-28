print("Enter the number of elements in the list:")
n = int(input())
print("Enter the elements of the list:")
elements = []
for i in range(n):
    elements.append(int(input()))
print("Enter the element to search for:")
target = int(input())

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

result = linear_search(elements, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")