# Aim: Implementation of Graph and Searching using Depth First Search (DFS)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    if start not in visited:
        visited.append(start)
        for neighbour in graph[start]:
            dfs(graph, neighbour, visited)
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

# Run DFS
if __name__ == "__main__":
    traversal = dfs(graph_data, 'A')
    print("Depth First Search traversal:", traversal)
