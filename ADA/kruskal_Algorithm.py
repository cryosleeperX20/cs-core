# Kruskal's Algorithm for Minimum Spanning Tree (MST)

import time

start = time.time()

def kruskal_algorithm(graph):
    n = len(graph)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):  # Avoid duplicate edges
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()
    parent = [i for i in range(n)]

    def find_parent(node):
        if parent[node] != node:
            parent[node] = find_parent(parent[node])
        return parent[node]

    def union(u, v):
        parent_u = find_parent(u)
        parent_v = find_parent(v)
        parent[parent_v] = parent_u

    mst = []
    for weight, u, v in edges:
        if find_parent(u) != find_parent(v):
            union(u, v)
            mst.append((u, v, weight))

    for u, v, weight in mst:
        print(f"Edge {u} - {v} with weight {weight}")

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

kruskal_algorithm(graph)

end = time.time()
print("Execution time: {:.3f} ms".format((end - start) * 1000))
