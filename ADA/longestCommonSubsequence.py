# Longest Common Subsequence (LCS) using Dynamic Programming

import time

# Record start time
start = time.time()

def lcs(X, Y):
    x = len(X)
    y = len(Y)
    L = [[0] * (y + 1) for _ in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[x][y]
    lcs_str = [""] * (index + 1)
    lcs_str[index] = ""

    i, j = x, y
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS of", X, "and", Y, "is", "".join(lcs_str))

# Test the function
lcs("AGGTAB", "GXTXAYB")
lcs("ABCDGH", "AEDFHR")

# Record end time
end = time.time()

# Print the execution time
print("Execution time: {:.3f} ms".format((end - start) * 1000))
