# Aim: 
# Given an array of distinct integers (candidates) and a target integer,
# find all unique combinations in candidates where the candidate numbers sum to the target.
# Each number in candidates may be used an unlimited number of times.
# Return the combinations in any order.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(list(path))
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                # include candidates[i]
                path.append(candidates[i])
                # since we can reuse the same number, we pass `i` again
                backtrack(i, path, remaining - candidates[i])
                # backtrack
                path.pop()

        backtrack(0, [], target)
        return res
