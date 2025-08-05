#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int calculate(char* s) {
    int len = strlen(s);
    int* stack = (int*)malloc(sizeof(int) * len);
    int top = -1;
    int num = 0;
    char prevOp = '+';

    for (int i = 0; i <= len; i++) {
        char c = s[i];

        if (isdigit(c)) {
            num = num * 10 + (c - '0');
        }

        if ((!isdigit(c) && c != ' ') || i == len) {
            if (prevOp == '+') {
                stack[++top] = num;
            } else if (prevOp == '-') {
                stack[++top] = -num;
            } else if (prevOp == '*') {
                stack[top] = stack[top] * num;
            } else if (prevOp == '/') {
                stack[top] = stack[top] / num;
            }

            prevOp = c;
            num = 0;
        }
    }

    int result = 0;
    for (int i = 0; i <= top; i++) {
        result += stack[i];
    }

    free(stack);
    return result;
}

int main() {
    char expr[] = " 3+5 / 2 ";
    printf("Result: %d\n", calculate(expr)); // Output: 5
    return 0;
}
