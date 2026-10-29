# def tepi(x, y):
#     if not (0 <= x < len(bmp) and 0 <= y < len(bmp[0])): return
#     if bmp[x][y] != 255: return

#     bmp[x][y] = 253  # tanda sementara
#     is_edge = False
#     arah = [(0,1),(1,0),(0,-1),(-1,0)]  # kanan, bawah, kiri, atas

#     for dx, dy in arah:
#         nx, ny = x+dx, y+dy
#         if 0 <= nx < len(bmp) and 0 <= ny < len(bmp[0]):
#             if bmp[nx][ny] == 0: 
#                 is_edge = True
#             elif bmp[nx][ny] == 255: 
#                 tepi(nx, ny)

#     if is_edge:
#         bmp[x][y] = 125 
#     else :
#         bmp[x][y] = 255

def tepi(x, y):
    # stop bila keluar batas
    if x < 0 or x >= len(bmp) or y < 0 or y >= len(bmp[0]):
        return
    # hanya proses sel bernilai 255
    if bmp[x][y] != 255:
        return

    # tandai sementara biar tidak bolak-balik
    bmp[x][y] = 253
    is_edge = False
    print()
    for baris in range(len(bmp)):
        for kolom in range(len(bmp[baris])):
            print(bmp[baris][kolom], end='  ')
        print()
    print()

    # --- KANAN: (x, y+1)
    if y + 1 < len(bmp[0]):
        if bmp[x][y + 1] == 0:
            is_edge = True
        elif bmp[x][y + 1] == 255:
            tepi(x, y + 1)

    # --- BAWAH: (x+1, y)
    if x + 1 < len(bmp):
        if bmp[x + 1][y] == 0:
            is_edge = True
        elif bmp[x + 1][y] == 255:
            tepi(x + 1, y)

    # --- KIRI: (x, y-1)
    if y - 1 >= 0:
        if bmp[x][y - 1] == 0:
            is_edge = True
        elif bmp[x][y - 1] == 255:
            tepi(x, y - 1)

    # --- ATAS: (x-1, y)
    if x - 1 >= 0:
        if bmp[x - 1][y] == 0:
            is_edge = True
        elif bmp[x - 1][y] == 255:
            tepi(x - 1, y)

    # finalisasi: ubah jadi 125 kalau tepi, atau kembalikan jadi 255
    if is_edge:
        bmp[x][y] = 125 
    else :
        bmp[x][y] = 255

bmp = [[0,0,0,0,0],
       [0,255,255,255,0],
       [0,255,255,255,255],
       [0,255,255,255,0],
       [0,255,0,0,0]]
print('Sebelum Deteksi Tepi')
for baris in range(len(bmp)):
    for kolom in range(len(bmp[baris])):
        print(bmp[baris][kolom], end='  ')
    print()

for baris in range(len(bmp)):
    for kolom in range(len(bmp[baris])):
        if bmp[baris][kolom] == 255:
            kanan = (kolom + 1 < len(bmp[baris]) and bmp[baris][kolom + 1] == 0)
            bawah = (baris + 1 < len(bmp)       and bmp[baris + 1][kolom] == 0)
            kiri  = (kolom - 1 >= 0             and bmp[baris][kolom - 1] == 0)
            atas  = (baris - 1 >= 0             and bmp[baris - 1][kolom] == 0)
            if kanan or bawah or kiri or atas:
                tepi(baris,kolom) 
# Pengecekan di loop utama adalah Optimasi.Kode tetap bisa jalan tanpanya (secara teknis), tapi akan menjadi sangat lambat 
# pada gambar besar karena melakukan rekursi yang tidak perlu pada bagian tengah objek yang solid.
# jadi tujuannya untuk Masalah Efisiensi agar terpicu mulai dari terluar

print()
print('Deteksi Tepi')
for baris in range(len(bmp)):
    for kolom in range(len(bmp[baris])):
        print(bmp[baris][kolom], end='  ')
    print()