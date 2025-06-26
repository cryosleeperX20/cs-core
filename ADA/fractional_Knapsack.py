# Fractional Knapsack Problem using Greedy Algorithm

import time

# Record start time
start = time.time()

n = int(input("Enter the number of items: "))

values = []
weights = []

for i in range(n):
    values.append(int(input("Enter value of item {}: ".format(i + 1))))
for i in range(n):
    weights.append(int(input("Enter weight of item {}: ".format(i + 1))))

maxweight = int(input("Enter the maximum weight of the knapsack: "))

def fractionalKnapsack(n, values, weights, maxweight):
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))

    items.sort(reverse=True)

    total_value = 0

    for ratio, value, weight in items:
        if weight <= maxweight:
            total_value += value
            maxweight -= weight
        else:
            total_value += ratio * maxweight
            break

    return total_value

print("Maximum value in the knapsack:", fractionalKnapsack(n, values, weights, maxweight))

# Record end time
end = time.time()

print("Execution time: {:.3f} ms".format((end - start) * 1000))
