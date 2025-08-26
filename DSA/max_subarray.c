//find the maximum subarray sum using Kadane's algorithm

#include <stdio.h>

int maxSubArray(int* nums, int numsSize) {
    int maxSum = nums[0];
    int currSum = nums[0];

    for(int i = 1; i < numsSize; i++) {
        if(currSum + nums[i] > nums[i]) {
            currSum = currSum + nums[i];
        } else {
            currSum = nums[i];
        }

        if(currSum > maxSum) {
            maxSum = currSum;
        }
    }

    return maxSum;
}

int main() {
    int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
    int n = sizeof(arr)/sizeof(arr[0]);
    printf("%d\n", maxSubArray(arr, n));
    return 0;
}
