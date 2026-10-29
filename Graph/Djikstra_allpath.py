import heapq

def dijkstra_all_paths(graph, start):
    # Inisialisasi jarak dan jalur
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    pq = [(0, start)]  # (jarak, node)

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Jika jarak sekarang bukan jarak terbaik, lewati
        if current_dist > dist[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Rekonstruksi semua path dari prev
    paths = {}
    for node in graph:
        if dist[node] == float('inf'):
            paths[node] = None  # tidak terjangkau
            continue
        path =[]
        cur = node
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
            path.reverse()
            paths[node]= path

    return dist, paths


# Contoh graf (seperti diagram kamu)
graph = {
    "A" : {"B" : 2, "C" : 4},
    "B" : {"A" : 2, "C" : 1, "D" : 7},
    "C" : {"A" : 4, "B" : 1, "D" : 3},
    "D" : {"B" : 7, "C" : 3}
}

# Jalankan
dist, path = dijkstra_all_paths(graph, "A")

# Tampilkan Hasil
print("Hasil Dijkstra dari A:\n")
for node in sorted(graph.keys()):
    print(f"{node}: Distance = {dist[node]}, Path = {' -> '.join(path[node])}")