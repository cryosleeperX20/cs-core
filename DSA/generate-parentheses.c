// Aim: Generate all combinations of well-formed parentheses for given n pairs.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void backtrack(char **res, int *returnSize, char *cur, int open, int close, int max, int pos) {
    if (pos == max * 2) {
        cur[pos] = '\0';
        res[*returnSize] = strdup(cur);  // copy string into result
        (*returnSize)++;
        return;
    }
    if (open < max) {
        cur[pos] = '(';
        backtrack(res, returnSize, cur, open + 1, close, max, pos + 1);
    }
    if (close < open) {
        cur[pos] = ')';
        backtrack(res, returnSize, cur, open, close + 1, max, pos + 1);
    }
}

char **generateParenthesis(int n, int *returnSize) {
    int capacity = 10000; // upper bound for safety
    char **res = (char **)malloc(sizeof(char *) * capacity);
    *returnSize = 0;

    char *cur = (char *)malloc(sizeof(char) * (2 * n + 1));
    backtrack(res, returnSize, cur, 0, 0, n, 0);

    free(cur);
    return res;
}

// For local testing
int main() {
    int n = 3, returnSize;
    char **result = generateParenthesis(n, &returnSize);

    for (int i = 0; i < returnSize; i++) {
        printf("%s\n", result[i]);
        free(result[i]);
    }
    free(result);
    return 0;
}
