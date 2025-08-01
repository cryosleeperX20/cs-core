/*
LeetCode Problem 53: Maximum Subarray

🎯 Problem Aim:
Given an integer array `nums`, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

💡 Key Insight:
Use Kadane's Algorithm – maintain a running sum and reset it to 0 when it drops below 0.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6  (Because [4, -1, 2, 1] has the largest sum)
*/


#include <stdio.h>
#include <limits.h>

int maxSubArray(int* nums, int numsSize) {
    int max_sum = INT_MIN;
    int current_sum = 0;

    for (int i = 0; i < numsSize; i++) {
        current_sum += nums[i];
        if (current_sum > max_sum)
            max_sum = current_sum;
        if (current_sum < 0)
            current_sum = 0;
    }

    return max_sum;
}

int main() {
    int nums[] = {-2,1,-3,4,-1,2,1,-5,4};
    int size = sizeof(nums) / sizeof(nums[0]);
    int result = maxSubArray(nums, size);
    printf("Maximum Subarray Sum is: %d\n", result);
    return 0;
}
