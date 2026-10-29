def gridTraveler(m, n):            
    table = [[0 for column in range(n+1)] for row in range(m+1)] # +1 karena kita mau index 0 sebagai tanda ngga berjalan sehingga panjang kali lebarnya m+1 * n+1
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1): # ingat mulai dari index 0 
            if i+1 <= m: #arinya masih boleh sampai index ke m misal dlm contoh ini i adlah 2
                table[i+1][j] += table[i][j] #bisa dianggap seperti membuka jalan dimana jika bisa dilalui akan di tambah 1 dari nilai awal ke jalan tersebut
            if j+1 <= n:
                table[i][j+1] += table[i][j]                
    for i in table:
        print(i)
    return table[m][n]

print(gridTraveler(3,3))

