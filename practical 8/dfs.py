# Practical 8: Depth First Search (DFS)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()


def dfs(vertex):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor)


print("Graph:")
for vertex in graph:
    print(vertex, "->", graph[vertex])

print("\nDFS Traversal:")
dfs('A')

print()