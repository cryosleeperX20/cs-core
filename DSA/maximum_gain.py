# Problem: Maximum Score From Removing Substrings (LeetCode 1717)
# Aim: Remove substrings "ab" or "ba" to maximize score based on given point values.
# Approach:
# 1. Always remove the higher-value substring first ("ab" if x >= y, else "ba").
# 2. Use a single pass with a stack to greedily remove occurrences of the high-value substring.
# 3. Then process the remaining characters to remove the other substring with another stack pass.
# Time Complexity: O(n), Space Complexity: O(n)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Ensure we remove the more valuable pattern first
        first, second = ("a", "b") if x >= y else ("b", "a")
        first_val, second_val = (x, y) if x >= y else (y, x)

        # First pass: remove all occurrences of the top-valued substring
        stack1 = []
        score = 0
        for ch in s:
            if stack1 and stack1[-1] == first and ch == second:
                stack1.pop()
                score += first_val
            else:
                stack1.append(ch)

        # Second pass: remove the lower-valued substring from the remaining
        stack2 = []
        for ch in stack1:
            if stack2 and stack2[-1] == second and ch == first:
                stack2.pop()
                score += second_val
            else:
                stack2.append(ch)

        return score
