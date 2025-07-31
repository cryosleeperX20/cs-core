# Implemented solution for LeetCode Problem 224: Basic Calculator.
# - Parses and evaluates a mathematical expression containing '+', '-', '(', ')', and integers.
# - Handles nested parentheses and whitespace.
# - Uses a stack-based approach to maintain current signs and results during traversal.

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1
        result = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * num
                num = 0
                result *= stack.pop()  
                result += stack.pop() 

        result += sign * num
        return result
