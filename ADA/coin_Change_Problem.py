# Making Change Problem using Dynamic Programming

import time

# Record start time
start = time.time()

def making_change(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Test the function
coins = [1, 2, 5]
amount = 6
print("Amount of coins required:", making_change(coins, amount))

coins2 = [1, 2, 5]
amount2 = 8
print("Amount of coins required:", making_change(coins2, amount2))

# Record end time
end = time.time()

# Print the execution time
print("Execution time: {:.3f} ms".format((end - start) * 1000))
