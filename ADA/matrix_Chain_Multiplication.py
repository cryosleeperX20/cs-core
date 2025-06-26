# Chain Matrix Multiplication using Dynamic Programming

import time

# Record start time
start = time.time()

def chainMatrixMultiplication(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n - 1]

# Test the function
dimensions = [30, 35, 15, 5, 10]
result = chainMatrixMultiplication(dimensions)
print("Minimum number of scalar multiplications:", result)

# Record end time
end = time.time()

# Print the execution time
print("Execution time: {:.3f} ms".format((end - start) * 1000))
