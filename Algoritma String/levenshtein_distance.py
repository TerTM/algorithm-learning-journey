def levenshtein_distance(a, b):
    m, n = len(a), len(b)
    
    #Buat matriks kosong berukuran (m+1) * (n+1)
    dp = [[0]* (n+1) for _ in range(m+1)]

    #Inisialisasi baris dan kolom pertama
    for i in range(m+1):
        dp[i][0] = i
    
    for j in range(n+1):
        dp[0][j] = j

    # Isi Matriks
    for i in range(1,m +1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]: # cost = 0 if a[i-1] == b[j-1] else 1
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i-1][j] + 1, # Hapus
                dp[i][j-1] + 1, # Tambah
                dp[i-1][j-1] + cost, # ganti/subtitute
            )

    return dp[m][n]


kata1 = "buku"
kata2 = "baku"

hasil = levenshtein_distance(kata1, kata2)
print(f"Jarak Levenshtein antara {kata1} dengan {kata2} adalah {hasil}")