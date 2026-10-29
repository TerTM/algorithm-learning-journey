def bellman_ford(graph, source):
    # Inisialisasi jarak & parent
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    distance[source] = 0

    nodes = list(graph.keys())

    # Langkah 1: relaksasi sebanyak |V| - 1 kali
    for _ in range(len(nodes) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    parent[v] = u

    # Langkah 2: deteksi negative cycle
    for u in graph:
        for v, w in graph[u].items():
            if distance[u] + w < distance[v]:
                print("Graf memiliki siklus negatif!")
                return None

    # Langkah 3: rekonstruksi path
    print(f"=== HASIL BELLMAN-FORD (source: {source}) ===\n")
    for node in nodes:
        if distance[node] == float('inf'):
            print(f"{source} → {node} : tidak terjangkau")
        else:
            path = []
            current = node
            while current is not None:
                path.insert(0, current)
                current = parent[current]
            print(f"{source} → {node} : jarak = {distance[node]} | jalur: {' → '.join(path)}")

    return distance


# Contoh penggunaan
graph = {
    "A": {"B": 4, "C": 5},
    "B": {"D": -3},
    "C": {"D": 6},
    "D": {}
}

bellman_ford(graph, "A")
