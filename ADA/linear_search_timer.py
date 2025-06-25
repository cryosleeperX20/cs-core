# Linear Search Algorithm with Execution Time Analysis

import time  # Import time module

# Start the timer
start = time.time()

# Input: Number of elements
n = int(input("Enter the number of elements: "))

# Input: Array elements
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Input: Element to search
x = int(input("Enter the element to search: "))

# Linear Search Function
def linearSearch(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i  # Return index if found
    return -1  # Return -1 if not found

# Output: Result of the search
result = linearSearch(arr, n, x)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found.")

# End the timer
end = time.time()

# Print Execution Time in milliseconds
print("Execution time:", (end - start) * 1000, "ms")
