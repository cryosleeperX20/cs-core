# Implementation and Time Analysis of Factorial Program using Iterative and Recursive method
import time

# ------------------ Iterative Method ------------------

num_iter = int(input("Enter a number for Iterative Method: "))

start_iter = time.time()

# Factorial using Iterative Method
fact_iter = 1
for i in range(1, num_iter + 1):
    fact_iter *= i

# Record end time
end_iter = time.time()

# Print result and time
print("\n[ITERATIVE]")
print(f"Factorial of {num_iter} is: {fact_iter}")
print(f"Execution Time: {(end_iter - start_iter) * 1000:.5f} ms")

# ------------------ Recursive Method ------------------

# Define recursive factorial function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Take input from user
num_rec = int(input("\nEnter a number for Recursive Method: "))

# Record start time
start_rec = time.time()

# Compute factorial
fact_rec = factorial_recursive(num_rec)

# Record end time
end_rec = time.time()

# Print result and time
print("\n[RECURSIVE]")
print(f"Factorial of {num_rec} is: {fact_rec}")
print(f"Execution Time: {(end_rec - start_rec) * 1000:.5f} ms")
