
// Aim: Given numCourses and a list of prerequisite pairs, determine if you can finish all courses.
// This is equivalent to checking if a directed graph has a cycle (topological sort problem).

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool dfs(int** graph, int* graphColSize, int node, int* visited) {
    if (visited[node] == 1) return false; 
    if (visited[node] == 2) return true; 
    
    visited[node] = 1; 
    for (int i = 0; i < graphColSize[node]; i++) {
        if (!dfs(graph, graphColSize, graph[node][i], visited))
            return false;
    }
    visited[node] = 2; 
    return true;
}

bool canFinish(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize) {
    int** graph = (int**)malloc(sizeof(int*) * numCourses);
    int* graphColSize = (int*)calloc(numCourses, sizeof(int));
    
    for (int i = 0; i < numCourses; i++) {
        graph[i] = NULL;
    }

    for (int i = 0; i < prerequisitesSize; i++) {
        int course = prerequisites[i][0];
        int prereq = prerequisites[i][1];
        graph[prereq] = (int*)realloc(graph[prereq], sizeof(int) * (graphColSize[prereq] + 1));
        graph[prereq][graphColSize[prereq]++] = course;
    }

    int* visited = (int*)calloc(numCourses, sizeof(int)); // 0 = unvisited, 1 = visiting, 2 = done
    for (int i = 0; i < numCourses; i++) {
        if (visited[i] == 0) {
            if (!dfs(graph, graphColSize, i, visited)) {
                for (int j = 0; j < numCourses; j++) free(graph[j]);
                free(graph);
                free(graphColSize);
                free(visited);
                return false;
            }
        }
    }

    for (int i = 0; i < numCourses; i++) free(graph[i]);
    free(graph);
    free(graphColSize);
    free(visited);
    return true;
}

int main() {
    int numCourses = 4;
    int prereqArr[4][2] = {{1,0},{2,1},{3,2},{1,3}}; // introduces a cycle
    int prerequisitesSize = 4;
    int prerequisitesColSize[4] = {2,2,2,2};
    
    int* prerequisites[4];
    for (int i = 0; i < prerequisitesSize; i++) {
        prerequisites[i] = prereqArr[i];
    }
    
    if (canFinish(numCourses, prerequisites, prerequisitesSize, prerequisitesColSize))
        printf("All courses can be finished.\n");
    else
        printf("Cannot finish all courses (cycle detected).\n");
    
    return 0;
}
