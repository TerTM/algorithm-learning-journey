import heapq

def greedy_best_first(graph_data, start, goal): #ambbil dari nilai heuristik terkecil
    pq = [(graph_data[start]['h'], start, [start])]
    visited = set()

    while pq:
        print(pq)
        _, node, path = heapq.heappop(pq) #heapqm otomatis mengambil terkecil
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)

        for nb in graph_data[node]['neighbors']:
            if nb not in visited:
                heapq.heappush(pq, (graph_data[nb]['h'], nb, path+ [nb]))
    return None

graph_data = {
    'A': {'neighbors': ['B', 'C'], 'h':3},
    'B': {'neighbors': ['A', 'D', 'E'], 'h':2},
    'C': {'neighbors': ['A'], 'h':4},
    'D': {'neighbors': ['B'], 'h':4},
    'E': {'neighbors': ['B', 'F'], 'h':1},
    'F': {'neighbors': ['E'], 'h':0},
}

path = greedy_best_first(graph_data, 'A', 'F')
print("Jalur Heuristik: ", path)