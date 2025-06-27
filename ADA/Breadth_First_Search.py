# Implementation of Graph and Searching : Breadth First Search

import time

# Record start time
start = time.time()

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

# Graph structure as adjacency list
graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS
result = bfs(graph_data, 'A')
print("Breadth First Search traversal:", result)

# Record end time
end = time.time()
print("Execution time: ", (end - start) * 1000, "ms")
