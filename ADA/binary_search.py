# Binary Search Algorithm: Iterative and Recursive with Execution Time Analysis

import time

# - Iterative Binary Search -

# Input from user
n = int(input("Enter the number of elements (sorted): "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

x = int(input("Enter the element to search (iterative): "))

# Start timer
start = time.time()

# Iterative Binary Search Function
def binary_search_iterative(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Call function
result = binary_search_iterative(arr, x)

# End timer and print result
end = time.time()
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
print("Iterative Method Execution Time:", (end - start) * 1000, "ms")

# - Recursive Binary Search -

# Re-input for fresh execution
n = int(input("\nEnter the number of elements (sorted): "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

x = int(input("Enter the element to search (recursive): "))

# Start timer
start = time.time()

# Recursive Binary Search Function
def binary_search_recursive(arr, x, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search_recursive(arr, x, mid + 1, high)
    else:
        return binary_search_recursive(arr, x, low, mid - 1)

# Call function
result = binary_search_recursive(arr, x, 0, n - 1)

# End timer and print result
end = time.time()
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")
print("Recursive Method Execution Time:", (end - start) * 1000, "ms")
