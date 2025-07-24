# Implemented solution for LeetCode Problem 71: Simplify Path.
# - Parses a Unix-style absolute path and simplifies it by resolving "." and ".." directory references.
# - Uses a stack to manage valid directory names and construct the canonical path.
# - Returns the simplified canonical path as a string.
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')
        
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        
        return '/' + '/'.join(stack)
