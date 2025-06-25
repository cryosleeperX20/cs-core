# Merge Sort Algorithm with Execution Time Analysis

import time

# Input Section
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))

# Start Timer
start = time.time()

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]     # Left half
        R = arr[mid:]     # Right half

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge the two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements of L[]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy remaining elements of R[]
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Run and Print Result
sorted_array = merge_sort(arr)
print("Sorted Array:", sorted_array)

# End Timer
end = time.time()
print("Execution Time:", (end - start) * 1000, "ms")
