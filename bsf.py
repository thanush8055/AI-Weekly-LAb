# BFS implementation in Python
from collections import deque

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = set()        # To keep track of visited nodes
    queue = deque([start]) # Queue for BFS

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Start BFS from node A
print("BFS Traversal:")
bfs(graph, 'A')