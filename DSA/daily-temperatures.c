// Aim: For each day, find how many days you would have to wait until a warmer temperature.
// If there is no such day, output 0 for that day.

#include <stdio.h>
#include <stdlib.h>

int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize) {
    int *res = (int *)calloc(temperaturesSize, sizeof(int));
    int *stack = (int *)malloc(sizeof(int) * temperaturesSize); // stack for indices
    int top = -1;

    for (int i = 0; i < temperaturesSize; i++) {
        while (top >= 0 && temperatures[i] > temperatures[stack[top]]) {
            int idx = stack[top--];
            res[idx] = i - idx;
        }
        stack[++top] = i;
    }

    free(stack);
    *returnSize = temperaturesSize;
    return res;
}

int main() {
    int temps[] = {73, 74, 75, 71, 69, 72, 76, 73};
    int n = sizeof(temps) / sizeof(temps[0]);
    int returnSize;

    int *result = dailyTemperatures(temps, n, &returnSize);

    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    free(result);
    return 0;
}
