from collections import deque

def solve_aerobot_bfs(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    start = None
    goal = None
    
    # 1. Cari posisi Start (2) dan Goal (3)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                start = (r, c)
            elif grid[r][c] == 3:
                goal = (r, c)
                
    if not start or not goal:
        return "Start atau Goal tidak ditemukan."

    # Arah pergerakan: Atas, Bawah, Kiri, Kanan (Baris, Kolom)
    # Tidak ada diagonal
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 2. Inisialisasi BFS
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    # Dictionary untuk melacak dari mana kita datang (untuk rekonstruksi jalur nanti)
    came_from = {start: None}
    
    found = False
    
    # 3. Loop BFS
    while queue:
        current = queue.popleft() # Ambil elemen pertama (FIFO)
        
        # Jika sampai di tujuan
        if current == goal:
            found = True
            break
        
        # Cek 4 arah tetangga
        cur_r, cur_c = current
        for dr, dc in directions:
            next_r, next_c = cur_r + dr, cur_c + dc
            
            # Cek validitas: dalam batas grid, bukan dinding (1), dan belum dikunjungi
            if 0 <= next_r < rows and 0 <= next_c < cols:
                if grid[next_r][next_c] != 1 and (next_r, next_c) not in visited:
                    queue.append((next_r, next_c))
                    visited.add((next_r, next_c))
                    came_from[(next_r, next_c)] = current
    
    if not found:
        return "Jalur tidak ditemukan."
    
    # 4. Rekonstruksi Jalur (Backtracking dari Goal ke Start)
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = came_from[curr]
    
    path.reverse() # Balik urutan agar dari Start -> Goal
    return path

# --- Data Peta Museum ---
museum_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 3],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1],
]

# --- Jalankan Program ---
path = solve_aerobot_bfs(museum_grid)

# --- Output ---
if isinstance(path, list):
    print(f"Jalur ditemukan dengan {len(path) - 1} langkah:")
    for step, coord in enumerate(path):
        item = "START" if step == 0 else ("GOAL" if step == len(path)-1 else "Jalan")
        print(f"Langkah {step}: {coord} - {item}")
        
    print("\nVisualisasi Jalur pada Peta:")
    # Membuat visualisasi sederhana
    visual_grid = [row[:] for row in museum_grid] # Copy grid
    for r, c in path:
        if visual_grid[r][c] not in [2, 3]:
            visual_grid[r][c] = '.' # Tandai jalur dengan titik
            
    for row in visual_grid:
        # Mengubah angka menjadi karakter agar lebih mudah dilihat
        print(" ".join(str(x).replace('1', '|').replace('0', ' ').replace('.', '.') for x in row))
else:
    print(path)