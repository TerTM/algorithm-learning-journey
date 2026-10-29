import heapq

def djikstra(graph, start, goal): #ambil dari ni.ai edge terkecil
    dist = {v: float('inf') for v in graph}
    prev = {v: None for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq) #heapqm otomatis mengambil terkecil
        if u == goal:
            break
        if d != dist[u]:
            continue

        for v, w in graph[u].items():
            nd = d + w 
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd,v))
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    return path, dist[goal]

#graf tak berarah A 'ke B = 2 
graph = {
    'A': {'B': 2, 'C':4},
    'B': {'A': 2, 'C':1, 'D':7},
    'C': {'A': 4, 'B':1, 'D':3},
    'D': {'B':7, 'C':3}
    
}

path,total = djikstra(graph, 'A', 'D')
print("Jalur : ", "-> ".join(path))
print("Jarak : ", total)