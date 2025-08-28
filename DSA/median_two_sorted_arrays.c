//find the median of two sorted arrays by merging until the middle
#include <stdio.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int m = nums1Size, n = nums2Size;
    int total = m + n;
    int mid1 = (total - 1) / 2;
    int mid2 = total / 2;
    int i = 0, j = 0, count = 0;
    int a = 0, b = 0;

    while (count <= mid2) {
        int val;
        if (i < m && (j >= n || nums1[i] <= nums2[j])) {
            val = nums1[i++];
        } else {
            val = nums2[j++];
        }

        if (count == mid1) a = val;
        if (count == mid2) b = val;
        count++;
    }

    return (a + b) / 2.0;
}

int main() {
    int nums1[] = {1, 3};
    int nums2[] = {2};
    int size1 = sizeof(nums1) / sizeof(nums1[0]);
    int size2 = sizeof(nums2) / sizeof(nums2[0]);

    double median = findMedianSortedArrays(nums1, size1, nums2, size2);
    printf("%f\n", median);
    return 0;
}
