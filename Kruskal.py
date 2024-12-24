# -*- coding: utf-8 -*-
class union_find:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(ve, ed):
    # Sort edges by weight
    ed.sort(key=lambda x: x[2])
    uf = union_find(ve)
    mst = []
    weightmst = 0

    for u, v, w in ed:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, w))
            weightmst += w

    return mst, weightmst

vertices = int(input("Enter number of vertices "))
edges = []
n = int(input("Enter the number of edges: "))
print("Enter the edges")
for i in range(n):
    u, v, w = map(int, input("Edge: ").split())
    edges.append((u, v, w))

mst, mstWeight = kruskal(vertices, edges)
print("Edges in MST:", mst)
print("weight of MST:", mstWeight)


