# Prim's Algorithm for Minimum Spanning Tree (MST)

import time

start = time.time()

def prims_algorithm(graph):
    n = len(graph)
    mst = [False] * n
    mst[0] = True

    for _ in range(n - 1):
        min_edge = float('inf')
        u = v = -1
        for i in range(n):
            if mst[i]:
                for j in range(n):
                    if not mst[j] and graph[i][j] != 0 and graph[i][j] < min_edge:
                        min_edge = graph[i][j]
                        u, v = i, j
        mst[v] = True
        print(f"Edge {u} - {v} with weight {min_edge}")

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prims_algorithm(graph)

end = time.time()
print("Execution time: {:.3f} ms".format((end - start) * 1000))
