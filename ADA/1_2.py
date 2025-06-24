# Implementation and Time analysis of Sorting Algorithms: Selection Sort

import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    print("Selection Sort Implementation with Execution Time\n")

    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            print("Please enter a positive number.")
            return

        # Taking list input
        arr = []
        for i in range(n):
            val = int(input(f"Enter element {i + 1}: "))
            arr.append(val)

        # Timing the sort
        start_time = time.perf_counter()
        sorted_arr = selection_sort(arr)
        end_time = time.perf_counter()

        print("\n Sorted Array:", sorted_arr)
        print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")

    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
