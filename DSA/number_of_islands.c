
// Aim: Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

#include <stdio.h>
#include <stdlib.h>

void dfs(char** grid, int i, int j, int rows, int cols) {
    if (i < 0 || j < 0 || i >= rows || j >= cols || grid[i][j] != '1')
        return;
    grid[i][j] = '0';
    dfs(grid, i + 1, j, rows, cols);
    dfs(grid, i - 1, j, rows, cols);
    dfs(grid, i, j + 1, rows, cols);
    dfs(grid, i, j - 1, rows, cols);
}

int numIslands(char** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) return 0;
    int rows = gridSize;
    int cols = gridColSize[0];
    int count = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == '1') {
                count++;
                dfs(grid, i, j, rows, cols);
            }
        }
    }
    return count;
}

int main() {
    int rows = 4, cols = 5;
    char gridArr[4][5] = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };

    char** grid = (char**)malloc(rows * sizeof(char*));
    for (int i = 0; i < rows; i++) {
        grid[i] = (char*)malloc(cols * sizeof(char));
        for (int j = 0; j < cols; j++) {
            grid[i][j] = gridArr[i][j];
        }
    }

    int gridColSize[4] = {cols, cols, cols, cols};
    int islands = numIslands(grid, rows, gridColSize);

    printf("Number of islands = %d\n", islands);

    for (int i = 0; i < rows; i++) free(grid[i]);
    free(grid);
    return 0;
}
