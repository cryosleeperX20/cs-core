# Quick Sort Algorithm with Execution Time Analysis

import time

# Input section
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Start timer
start = time.time()

# Partition function
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Quick sort function
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Call quick sort
quick_sort(arr, 0, n - 1)

# Output sorted array
print("Sorted Array:", arr)

# End timer
end = time.time()
print("Execution Time:", (end - start) * 1000, "ms")
