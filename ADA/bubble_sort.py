# Implementation and Time analysis of Sorting Algorithms: Bubble Sort

#Importing Time Module for Execution Time Analysis
import time

start = time.time()

#Take Number of elements as input from the user
n = int(input("Enter the number of elements: "))

# Take the Elements in the Array from the user
arr = []
for i in range(n):
    arr.append(int(input("Enter the element: ")))

flag = 0;

# Sorting the Array using Bubble Sort
while(flag == 0):
    flag = 1
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = 0

print("Sorted Array: ", arr)

end = time.time()

print("The time of execution of above program is :",(end-start) * 10**3, "ms")
