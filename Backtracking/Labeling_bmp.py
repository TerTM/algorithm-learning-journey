def labeling(bmp, row, col, label):
    # 1) cek batas (agar indeks tidak keluar array)
    if row < 0 or row >= len(bmp) or col < 0 or col >= len(bmp[0]):
        return

    # 2) jika bukan bagian objek (bukan 1), hentikan
    #    (ini juga mencegah memproses ulang pixel yang sudah dilabel)
    if bmp[row][col] != 1:
        return

    # 3) tandai pixel ini dengan label (mis. 2,3,4,...)
    bmp[row][col] = label

    # 4) rekursi ke empat arah (atas, bawah, kiri, kanan)
    labeling(bmp, row+1, col, label)
    labeling(bmp, row-1, col, label)
    labeling(bmp, row, col+1, label)
    labeling(bmp, row, col-1, label)

def hitung_objek(bmp):
    if not bmp or not bmp[0]:
        return 0

    label = 2      # mulainya 2 (0=background, 1=foreground belum dilabel)
    jumlah = 0

    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            if bmp[i][j] == 1:          # ketemu bagian objek yang belum dilabel
                labeling(bmp, i, j, label)
                jumlah += 1
                label += 1
    return jumlah

bmp = [
  [0, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 0, 0, 1],
  [1, 0, 0, 1]
]

jumlah = hitung_objek(bmp)
print(jumlah)

for row in bmp:
    print(row)