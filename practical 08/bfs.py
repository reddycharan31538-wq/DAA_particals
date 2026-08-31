# Practical 8: Breadth First Search (BFS)

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def bfs(start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("Graph:")
for vertex in graph:
    print(vertex, "->", graph[vertex])

print("\nBFS Traversal:")
bfs('A')

print()