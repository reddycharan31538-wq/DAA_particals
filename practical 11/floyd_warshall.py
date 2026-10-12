
# Practical 11: Floyd-Warshall Algorithm
# All-Pairs Shortest Paths

INF = float("inf")


def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


print("=" * 50)
print("       FLOYD-WARSHALL ALGORITHM")
print("        ALL-PAIRS SHORTEST PATHS")
print("=" * 50)

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix (use 999 for no edge):")
graph = []

for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))

    if len(row) != n:
        print(f"Error: Enter exactly {n} values per row.")
        raise SystemExit

    graph.append([INF if x == 999 else x for x in row])

dist = floyd_warshall(graph)

print("\nShortest Distance Matrix:")
for row in dist:
    print(" ".join("INF" if x == INF else str(int(x)) for x in row))

print("\nTime Complexity: O(V^3)")
print("Space Complexity: O(V^2)")
print("=" * 50)
