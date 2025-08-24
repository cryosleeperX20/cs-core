
// Aim: Implement Dijkstra's Algorithm to calculate network delay time (Single Source Shortest Path problem).

#include <stdio.h>
#include <stdlib.h>

#define INF 1000000000   // Large value representing infinity

int networkDelayTime(int** times, int timesSize, int* timesColSize, int n, int k){
    int graph[101][101];
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            graph[i][j] = INF;
    
    for (int i = 0; i < timesSize; i++) {
        int u = times[i][0];
        int v = times[i][1];
        int w = times[i][2];
        graph[u][v] = w;
    }

    int dist[101], visited[101];
    for (int i = 1; i <= n; i++) {
        dist[i] = INF;
        visited[i] = 0;
    }
    dist[k] = 0;

    for (int i = 1; i <= n; i++) {
        int u = -1;
        for (int j = 1; j <= n; j++) {
            if (!visited[j] && (u == -1 || dist[j] < dist[u]))
                u = j;
        }
        if (u == -1 || dist[u] == INF) return -1;
        visited[u] = 1;

        for (int v = 1; v <= n; v++) {
            if (graph[u][v] < INF && dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (dist[i] == INF) return -1;
        if (dist[i] > ans) ans = dist[i];
    }
    return ans;
}


int main() {
    int edges[3][3] = {{2,1,1}, {2,3,1}, {3,4,1}};
    int* times[3];
    for (int i = 0; i < 3; i++) times[i] = edges[i];
    int timesColSize[3] = {3,3,3};

    int n = 4, k = 2;
    int result = networkDelayTime(times, 3, timesColSize, n, k);
    printf("Network delay time = %d\n", result);

    return 0;
}
