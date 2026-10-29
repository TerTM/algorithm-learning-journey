bmp = [[0,0,0,0,0],[0,255,255,255,255],[0,255,255,255,255],[0,255,255,255,0],[0,0,0,0,0]]

def labeling(bmp, i, j,a = 0):
    if j < 0 or j >= len(bmp[0]) or i < 0 or i >= len(bmp):
        return

    if bmp[i][j] == 0:
        return False
    
    if a>=1:
        if bmp[i][j] == 255:
            return True
        
    if labeling(bmp, i+1, j, a+1) == False: # Jika tetangga bawah menemukan 0
        return False # Maka fungsi ini ikut berhenti
    if labeling(bmp, i-1, j, a+1) == False:
        return False
    if labeling(bmp, i, j+1, a+1) == False:
        return False
    if labeling(bmp, i, j-1, a+1) == False:
        return False

    print("tes")
    bmp[i][j] = 125

def ubah(bmp):
    for i in range(len(bmp)):
        for j in range(len(bmp[0])):
            if bmp[i][j] == 255:
                labeling(bmp, i, j)

ubah(bmp)

for row in bmp:
    print(row)