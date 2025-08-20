// Aim: Count the number of ways to assign + or - signs to array elements 
// such that the total sum equals the given target.
// Approach: Convert to subset sum problem and solve using DP.

#include <stdio.h>
#include <stdlib.h>

int findTargetSumWays(int* nums, int numsSize, int target) {
    int total = 0;
    for (int i = 0; i < numsSize; i++) total += nums[i];

    if ((total + target) % 2 != 0 || abs(target) > total) return 0;

    int sum = (total + target) / 2;
    int *dp = (int *)calloc(sum + 1, sizeof(int));
    dp[0] = 1;

    for (int i = 0; i < numsSize; i++) {
        for (int j = sum; j >= nums[i]; j--) {
            dp[j] += dp[j - nums[i]];
        }
    }

    int result = dp[sum];
    free(dp);
    return result;
}

int main() {
    int nums[] = {1, 1, 1, 1, 1};
    int n = sizeof(nums) / sizeof(nums[0]);
    int target = 3;

    int ways = findTargetSumWays(nums, n, target);
    printf("Number of ways: %d\n", ways);

    return 0;
}
