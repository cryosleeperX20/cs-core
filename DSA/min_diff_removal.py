import heapq
import math
from typing import List
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        prefix_sum = 0
        max_heap = []
        min_left = [0] * len(nums)
        
        for i in range(2 * n):
            prefix_sum += nums[i]
            heapq.heappush(max_heap, -nums[i])
            if len(max_heap) > n:
                prefix_sum += heapq.heappop(max_heap)
            if len(max_heap) == n:
                min_left[i] = prefix_sum
        
        suffix_sum = 0
        min_heap = []
        result = math.inf
        
        for i in range(len(nums) - 1, n - 1, -1):
            suffix_sum += nums[i]
            heapq.heappush(min_heap, nums[i])
            if len(min_heap) > n:
                suffix_sum -= heapq.heappop(min_heap)
            if len(min_heap) == n:
                result = min(result, min_left[i - 1] - suffix_sum)
        
        return result
