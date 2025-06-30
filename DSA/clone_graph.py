# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned = {}  # Dictionary to keep track of visited/cloned nodes

        def dfs(curr):
            if curr in cloned:
                return cloned[curr]

            # Clone the current node (value only, neighbors will be added later)
            copy = Node(curr.val)
            cloned[curr] = copy

            # Now recursively clone all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
