# LeetCode 1695: Maximum Erasure Value
# Aim: Find the maximum sum of a subarray with all unique elements.
# Approach: Use sliding window and hash set to maintain a window with unique elements and track the max sum.

class Solution:
    def maximumUniqueSubarray(self, nums):
        seen = set()
        left = 0
        curr_sum = max_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)

        return max_sum
