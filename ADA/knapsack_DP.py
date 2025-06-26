# 0-1 Knapsack Problem using Dynamic Programming

import time

# Record start time
start = time.time()

# Input number of items
n = int(input("Enter the number of items: "))

# Input values
values = []
for i in range(n):
    values.append(int(input("Enter the value of item {}: ".format(i+1))))

# Input weights
weights = []
for i in range(n):
    weights.append(int(input("Enter the weight of item {}: ".format(i+1))))

# Input max weight of knapsack
maxweight = int(input("Enter the maximum weight capacity of the knapsack: "))

# 0-1 Knapsack DP function
def knapsack(n, values, weights, maxweight):
    dp = [[0 for _ in range(maxweight+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, maxweight+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][maxweight]

# Output the result
print("Maximum value in knapsack:", knapsack(n, values, weights, maxweight))

# Execution time
end = time.time()
print("Execution time: {:.3f} ms".format((end - start) * 1000))
