bmp = [[0,0,0,0,0],[0,255,255,255,255],[0,255,255,255,255],[0,255,255,255,0],[0,0,0,0,0]]

#Membuat hanya 255 jika atas kanan kiri bawahnya 255, dan mengubah yang bukan menjadi 125, 0 tetap 0

def labeling(bmp, i, j):
    if j < 0 or j >= len(bmp[0]) or i < 0 or i >= len(bmp):
        return
    
    if bmp[i][j] != 255:
        return False
    
    bmp[i][j] = 125
    
    labeling(bmp, i+1, j)
    labeling(bmp, i-1, j)
    labeling(bmp, i, j+1)
    labeling(bmp, i, j-1)

def ubah(bmp):
    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            if bmp[i][j] == 255:
                labeling(bmp, i, j)

ubah(bmp)

for row in bmp:
    print(row)