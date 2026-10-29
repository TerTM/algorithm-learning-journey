def find_next_empty(puzzle):
    for r in range(9): 
        for c in range(9):
            if puzzle[r][c] == -1:       #-1 artinya ada yang kosong
                return r, c
    return None, None

def is_valid(puzzle, row, col, check):
    #cek apakah dibaris yang sama ada angka yang sama
    row_vals = puzzle[row]
    if check in row_vals:
        return False
        
    #cek kolom
    for j in range(9):
        if puzzle[j][col] == check:
            return False
        
    # untuk menggeceK di kotak 3*3 kita akan membaginya dengan 3 sehingga bisa menentukan dia masuk ke salah satu dari 3 bagian(0, 1,2)
    # cth 0 // 3 = 0    1//3 = 0     2 // 3 = 0         3 // 3 = 1       4 // 3 =  1       5 // 3 = 1 dst
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if puzzle[i][j] == check:
                return False
            
    #jika sampai baris ini maka valid        
    return True

def solve_sudoku(puzzle):
    #1 cari apakah ada yang kosong di grid sudoku
    row, col = find_next_empty(puzzle)

    #1.1 kalau tidak ada yang kosong alias saat fungsi melakukan return none, maka program selesai
    if row == None:
        return True
    
    #2. mengambil angka 1-9 lalu mengecek apakah valid di posisi tersebut
    for guess in range(1, 10):
        
        if is_valid(puzzle, row, col, guess): # jika valid kita tetapkan guess di grid
            puzzle[row][col] = guess
            #jika valid kita bisa lakukan rekursi 
            if solve_sudoku(puzzle) == True:
                return True
        
        #kalau tidak valid atau guess kita tidak menemukan solusi maka kita akan coba dengan angka lain dan backtrack dengan reset angkanya
        puzzle[row][col] = -1

    #jika semua sudah di coba maka sudoku tidak bisa diselesaikan
    return False

puz = [[-1,5,1,3,-1,9,-1,-1,6], 
              [-1,2,-1,8,7,1,3,4,5],
              [-1,-1,-1,2,-1,-1,-1,-1,-1],
              [2,1,9,7,6,4,-1,3,-1],
              [-1,-1,-1,1,3,-1,-1,-1,-1],
              [7,3,-1,-1,-1,8,-1,6,2],
              [5,-1,-1,4,2,-1,-1,-1, 3],
              [-1,-1,-1,9,1,5,-1,-1,7],
              [1,9,-1,-1,-1,-1,2,-1,-1]]
print(solve_sudoku(puz))

for row in puz:
    print(row)







