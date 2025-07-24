# Implemented solution for "Minimum Score After Removals on a Tree" (LeetCode 2322).
# - Constructs the tree from given edges and performs DFS to compute XOR values of subtrees.
# - Evaluates all pairs of non-overlapping edges to determine minimum score.
# - Score is defined as the difference between max and min of XOR values of resulting three components.
# - Efficient use of DFS traversal and prefix computation to minimize redundant operations.

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        xor = [0] * n
        tin = [0] * n
        tout = [0] * n
        time = [0]

        # First DFS: calculate xor values and entry/exit times for each node
        def dfs(u, p):
            time[0] += 1
            tin[u] = time[0]
            xor[u] = nums[u]
            for v in tree[u]:
                if v != p:
                    dfs(v, u)
                    xor[u] ^= xor[v]
            time[0] += 1
            tout[u] = time[0]
        
        dfs(0, -1)
        total_xor = xor[0]

        # Helper to check if u is ancestor of v
        def is_ancestor(u, v):
            return tin[u] < tin[v] and tout[u] > tout[v]

        min_score = float('inf')
        
        # Try all pairs of edges (i.e., pairs of subtrees)
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = i, j
                if is_ancestor(a, b):
                    x = xor[b]
                    y = xor[a] ^ xor[b]
                    z = total_xor ^ xor[a]
                elif is_ancestor(b, a):
                    x = xor[a]
                    y = xor[b] ^ xor[a]
                    z = total_xor ^ xor[b]
                else:
                    x = xor[a]
                    y = xor[b]
                    z = total_xor ^ xor[a] ^ xor[b]
                min_score = min(min_score, max(x, y, z) - min(x, y, z))
        
        return min_score
