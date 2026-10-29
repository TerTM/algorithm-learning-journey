# DP bottom up
def warp(i, lwarp):
    lwarp[1] = 2
    lwarp[2] = 7

    if i >= 3:
        lwarp[i] = 3*lwarp[i-1] -  lwarp[i-2]
    return lwarp[i]

lwarp = [0] * 11

for i in range(1, 11):
    print(warp(i, lwarp))
    print(lwarp)

#VERSI GEMINI
memo_table = {}

def warp(n):
    # Cek apakah nilai n sudah ada di tabel memori
    if n in memo_table:
        return memo_table[n]

    # Base Case (Kondisi Dasar) sesuai soal
    if n == 1:
        return 2
    elif n == 2:
        return 7
    
    # Recursive Rule (Rumus Rekursif)
    # W(n) = 3 * W(n-1) - W(n-2)
    hasil = 3 * warp(n - 1) - warp(n - 2)
    
    # Simpan hasil perhitungan ke dalam tabel memori sebelum dikembalikan
    memo_table[n] = hasil
    
    return hasil

# PROGRAM UTAMA
# Loop dari 1 sampai 10 sesuai permintaan soal
print("GEMINI")
for i in range(1, 11):
    print(warp(i))

print(memo_table)
