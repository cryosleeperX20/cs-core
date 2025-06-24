# Implementation and Time analysis of Sorting Algorithms: Insertion Sort

import time

# Start the timer
start = time.time()

# Input number of elements
n = int(input("Enter the number of elements: "))

# Input array elements
arr = []
for _ in range(n):
    arr.append(int(input("Enter the element: ")))

# Insertion Sort algorithm
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

# Output sorted array
print("Sorted Array:", arr)

# End the timer and display execution time
end = time.time()
print("Execution Time: {:.3f} ms".format((end - start) * 1000))

