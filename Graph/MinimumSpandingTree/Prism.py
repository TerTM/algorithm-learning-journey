import heapq

def prim_mst(graph, start):
    visited = set([start])
    edges_heap = []

    #Masukkan semua edge dqri simpul awal
    for v, w in graph[start].items():
        heapq.heappush(edges_heap,(w, start, v))

    mst = []
    total_weight = 0

    while edges_heap and len(visited) < len(graph):
        w, u, v = heapq.heappop(edges_heap)
        if v in visited:
            continue

        visited.add(v)
        mst.append((u, v, w))
        total_weight += w

        #masukkan semua edge dari node baru
        for nxt, w2 in graph[v].items():
            if nxt not in visited:
                heapq.heappush(edges_heap, (w2, v, nxt))
    return mst, total_weight
    
graph = {
    'A':{'B':2, 'C':3},
    'B':{'A':2, 'C':1},
    'C':{'A':3, 'B':1}
}

graph = {
    'A': {'B':4,'C':2,'D':6},
    'B': {'A':4,'C':3,'E':7},
    'C': {'A':2,'B':3, 'D':5},
    'D': {'A':6,'C':5,'E':4},
    'E': {'B':7,'D':4}
}

mst, total = prim_mst(graph, start='A')

print('MST (Prism) : ', mst)
print("Total bobot : ", total)