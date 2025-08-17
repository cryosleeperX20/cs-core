
// Aim: Merge all overlapping intervals and return non-overlapping intervals.

#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    int* x = *(int**)a;
    int* y = *(int**)b;
    return x[0] - y[0];
}

int** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {
    if (intervalsSize == 0) {
        *returnSize = 0;
        *returnColumnSizes = NULL;
        return NULL;
    }
    
    qsort(intervals, intervalsSize, sizeof(int*), cmp);
    
    int** res = (int**)malloc(sizeof(int*) * intervalsSize);
    *returnColumnSizes = (int*)malloc(sizeof(int) * intervalsSize);
    int count = 0;
    
    res[count] = (int*)malloc(sizeof(int) * 2);
    res[count][0] = intervals[0][0];
    res[count][1] = intervals[0][1];
    (*returnColumnSizes)[count] = 2;
    
    for (int i = 1; i < intervalsSize; i++) {
        if (intervals[i][0] <= res[count][1]) {
            if (intervals[i][1] > res[count][1]) {
                res[count][1] = intervals[i][1];
            }
        } else {
            count++;
            res[count] = (int*)malloc(sizeof(int) * 2);
            res[count][0] = intervals[i][0];
            res[count][1] = intervals[i][1];
            (*returnColumnSizes)[count] = 2;
        }
    }
    
    *returnSize = count + 1;
    return res;
}

int main() {
    int intervalsArr[4][2] = {{1,3},{2,6},{8,10},{15,18}};
    int* intervals[4];
    for (int i = 0; i < 4; i++) intervals[i] = intervalsArr[i];
    int intervalsColSize[4] = {2,2,2,2};
    int returnSize;
    int* returnColSizes;
    
    int** merged = merge(intervals, 4, intervalsColSize, &returnSize, &returnColSizes);
    
    printf("Merged intervals:\n");
    for (int i = 0; i < returnSize; i++) {
        printf("[%d, %d]\n", merged[i][0], merged[i][1]);
        free(merged[i]);
    }
    free(merged);
    free(returnColSizes);
    return 0;
}
