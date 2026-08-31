# Practical 9: Implementation of Prim's Algorithm

INF = 999999
V = 5

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]


def prim_mst(graph):
    selected = [False] * V
    selected[0] = True

    print("Edges in Minimum Spanning Tree:")
    total_cost = 0

    for _ in range(V - 1):
        minimum = INF
        x = 0
        y = 0

        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(f"{x + 1} - {y + 1} : {minimum}")
        total_cost += minimum
        selected[y] = True

    print("Total cost:", total_cost)


print("Graph:")
for row in graph:
    print(row)

print()
prim_mst(graph)