"""
LeetCode 34 – Find First and Last Position of Element in Sorted Array

📝 Problem:
Given a sorted list of integers `nums` and a target value, find the starting and ending position 
of the target in the list. If the target is not present, return [-1, -1].

✅ Goal:
Use binary search to achieve O(log n) time complexity.
"""

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        if left <= right:
            return [left, right]
        return [-1, -1]
