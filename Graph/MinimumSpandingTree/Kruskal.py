# Struktur bantu Union-Find untuk deteksi siklus
class UnionFind:
    def __init__(self, nodes):
        self.parent = {x: x for x in nodes}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False # Sudah terhubung -> membentuk siklus
        self.parent[root_b] = root_a
        return True
    
def kruskal_mst(edges, nodes):
    #Urutkan edge berdasarkan bobot
    edges.sort(key=lambda x:x[2])
    uf = UnionFind(nodes)
    mst = []
    total_weight = 0

    for u,v,w in edges:
        if uf.union(u, v): #jika tidak membentuk siklus
            mst.append((u, v, w))
            total_weight += w

        #jika sudah V-1 edge, berhenti
        if len(mst) == len(nodes) -1:
            break
    return mst, total_weight

nodes = ['A', 'B', 'C']
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1)
]

nodes = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('A', 'D', 6),
    ('B', 'C', 3),
    ('B', 'E', 7), 
    ('C', 'D', 5),
    ('D', 'E', 4), 
]

mst, total = kruskal_mst(edges, nodes)

print("MST (Kruskal) : ", mst)
print("Total bobot : ", total)