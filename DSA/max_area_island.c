
// Find max area of island in a grid using DFS

#include <stdio.h>

int dfs(int **grid, int m, int *n, int i, int j) {
    if (i < 0 || j < 0 || i >= m || j >= n[i] || grid[i][j] == 0) {
        return 0;
    }
    grid[i][j] = 0; 
    int cnt = 1;
    cnt += dfs(grid, m, n, i+1, j);
    cnt += dfs(grid, m, n, i-1, j);
    cnt += dfs(grid, m, n, i, j+1);
    cnt += dfs(grid, m, n, i, j-1);
    return cnt;
}

int maxAreaOfIsland(int **grid, int m, int *n) {
    int ans = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n[i]; j++) {
            if (grid[i][j] == 1) {
                int area = dfs(grid, m, n, i, j);
                if (area > ans) ans = area;
            }
        }
    }
    return ans;
}

int main() {
    int arr[4][5] = {
        {0,0,1,0,0},
        {0,1,1,1,0},
        {0,0,1,0,0},
        {1,0,0,0,1}
    };
    int m = 4, n[4] = {5,5,5,5};
    int *grid[4];
    for (int i = 0; i < m; i++) {
        grid[i] = arr[i];
    }

    int res = maxAreaOfIsland(grid, m, n);
    printf("Max area = %d\n", res);

    return 0;
}
