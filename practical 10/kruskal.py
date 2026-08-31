# Practical 10: Implementation of Kruskal's Algorithm

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal(vertices, edges):
    edges.sort(key=lambda edge: edge[2])

    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    print("Edges in Minimum Spanning Tree:")

    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total cost:", total_cost)


vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ('A', 'B', 2),
    ('A', 'D', 6),
    ('B', 'C', 3),
    ('B', 'D', 8),
    ('B', 'E', 5),
    ('C', 'E', 7),
    ('D', 'E', 9)
]

print("Graph edges:")

for u, v, weight in edges:
    print(f"{u} - {v} : {weight}")

print()

kruskal(vertices, edges)