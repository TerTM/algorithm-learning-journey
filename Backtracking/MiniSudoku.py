def find_empty(grid):
    for r in range(3):
        for c in range(3):
            if grid[r][c] == 0:
                return r,c
    return None

def valid(grid, r, c, val):
    #cek baris
    for j in range(3):
        if grid[r][j] == val:
            return False
        
    #cek kolom
    for i in range(3):
        if grid[i][c] == val:
            return False
    
    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty: #Kalau sudah tidak ada yang 0 maka selesai dan balik ke fungsi rekursif sebelumnya yang masih berisi non-tail
        return True
    r, c = empty
    for val in range(1, 4): #Proses mengecek satu2 ke yang field yang blm diisi
        if valid(grid, r, c, val):
            grid[r][c] = val
            if solve(grid):
                return True #Non tailnya
            grid[r][c] = 0
    return False

# 0 = Kosong
grid = [
    [0, 2, 0],
    [0, 0, 3],
    [1, 0 ,0],
]        
if solve(grid):
    for row in grid:
        print(row)
else:
    print("Tidak ada solusi.")
