import heapq
def aStar(graph, start, goal, heuristic): #mencari berdasarkan f(n) = g(n) + h(n) 
    #Priority queue berisi (f, g, node):                     g(n) jarak ke node 
    pq = [(heuristic[start], 0, start)]
    parent = {start: None}
    best_g = {start: 0}
    closed = set()

    while pq:
        f, g, node = heapq.heappop(pq)
        if node in closed:
            continue
        closed.add(node)

        if node == goal:
            #Rekonstruksi Path
            path = []
            cur = node
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            return path, g

        for nb, w in graph[node].items():
            tentative_g = g + w
            #Skip jika sudah ada g yang lebih baik
            if nb in best_g and tentative_g >= best_g[nb]:
                continue
            best_g[nb] = tentative_g
            parent[nb] = node
            f_nb = tentative_g + heuristic[nb]
            heapq.heappush(pq, (f_nb, tentative_g, nb))   

    return None, float('inf')   

graph = {
    'S' : {'A':1, 'B':4},
    'A' : {'S':1, 'C':2, 'D':5},
    'B' : {'S':4, 'D':1},
    'C' : {'A':2, 'G':3},
    'D' : {'A':5, 'B':1, 'G':2},
    'G': {}
}
h = {'S':7, 'A':6, 'B':3, 'C':2, 'D':1, 'G':0}

path, cost = aStar(graph, 'S', 'G', h)
print('Path terbaik: ', "-> ".join(path) if path else "(tidak ada)")
print("Total cost : ", cost )