def bellman_ford_path(graph, source, goal):
    # Kumpulkan semua node (aman jika ada node yang hanya muncul sebagai tetangga)
    nodes = set(graph.keys())
    for u in graph:
        nodes.update(graph[u].keys())
    nodes = sorted(nodes)

    # Inisialisasi jarak & parent
    INF = float('inf')
    distance = {n: INF for n in nodes}
    parent   = {n: None for n in nodes}
    if source not in distance:
        raise ValueError(f"Source '{source}' tidak ada di graf.")
    if goal not in distance:
        raise ValueError(f"Goal '{goal}' tidak ada di graf.")

    distance[source] = 0

    # Relaksasi sebanyak |V|-1 (dengan early stop jika tidak ada perubahan)
    for _ in range(len(nodes) - 1):
        changed = False
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] != INF and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    parent[v] = u
                    changed = True
        if not changed:
            break

    # Deteksi negative cycle
    for u in graph:
        for v, w in graph[u].items():
            if distance[u] != INF and distance[u] + w < distance[v]:
                raise ValueError("Graf memiliki negative cycle; jarak tidak terdefinisi.")

    # Rekonstruksi path untuk goal
    if distance[goal] == INF:
        print(f"{source} → {goal} : tidak terjangkau")
        return INF, None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    # Tampilkan hasil rapi
    print("=== HASIL BELLMAN-FORD ===")
    print(f"Sumber : {source}")
    print(f"Tujuan : {goal}")
    print(f"Jarak  : {distance[goal]}")
    print(f"Jalur  : {' → '.join(path)}")

    return distance[goal], path


# ===== Contoh penggunaan =====
graph = {
    "A": {"B": 4, "C": 5},
    "B": {"D": -3},
    "C": {"D": 6},
    "D": {}
}

bellman_ford_path(graph, source="A", goal="D")