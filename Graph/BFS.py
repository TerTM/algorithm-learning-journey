from collections import deque #double-ended queue struktur data seperti queue biasa, tapi bisa menambah dan menghapus elemen dari kedua ujungnya (depan dan belakang) dengan efisiensi tinggi.
#lebih efisien karena kompleksitas O(1) Karena di balik layar, deque menggunakan doubly linked list atau blok memori melingkar, bukan array biasa seperti list. 

def bfs_shortest_path(graph, start, goal): #BREAD FIRST SEARCH
    #queue berisi (node sekarang, path_samapai_sini)
    queue = deque([(start, [start])])   #diinisialisasi dengan kumpulan/list of tuple berisi (node, [jalur untuk sampai kesitu])
    visited = set()

    while queue:
        (node, path) = queue.popleft()
        if node not in visited:
            visited.add(node)
            #jika sudah sampai tujuan
            if node == goal:
                return path
            
            #tambahkan tentangga ke queue
            for neighbor in graph[node]: #mengakses set berisi tetangga2 dari node saat ini menggunakan key dari node saat ini
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

graph = {
    "A": {'B', 'C'},
    "B": {'A', 'D', 'E'},
    "C": {'A'},
    "D": {'B'},
    'E': {'B','F'},
    'F': {'E'}
}

path = bfs_shortest_path(graph, 'A', 'F')
print("Jalur terpendek : ", path)

#keunggulan BFS 
# Mengambil elemen terdepan (FIFO) sehingga ini memastikan traversal level by level sehingga jalur pertama yang ditemukan ke goal adalah jalur dengan jumlah edge terkecil.

#dari chatgpt. Keuntungan: tidak membuat banyak salinan path selama traversal → menghemat waktu & memori.
#bedanya tidak menyimpan path langsung, tapi membangun ulang jalur menggunakan dictionary parent
def bfs_shortest_path_predecessor(graph, start, goal):
    if start == goal:
        return [start]
    queue = deque([start])
    visited = {start}
    parent = {}  # parent[node] = predecessor

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                if neighbor == goal:
                    # reconstruct path
                    path = [goal]
                    while path[-1] != start:
                        path.append(parent[path[-1]])
                    return path[::-1]
                queue.append(neighbor)
    print(parent)
    return None
a = bfs_shortest_path_predecessor(graph, 'A', 'F')
