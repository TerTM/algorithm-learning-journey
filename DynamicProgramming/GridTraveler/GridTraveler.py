def gridtraveler(row, column):
    if row == 0 or column == 0:
        return 0
    if row == 1 and column == 1:
        return 1
    return gridtraveler(row-1, column) + gridtraveler(row, column-1)          

print(gridtraveler(3,2))             

 #pada python {} dictionary sekali dibuat maka setelahnya akan menggunakan dictionary yang sama untuk rekursifnya
def GridTraveler(row, column, memo = {}): #
    if row == 0 or column == 0:
        return 0
    temp = str(min(column, row))+"*"+str(max(column,row)) # karena jumlah Solusi yang didapatkan dari row * Column = Column * Row 
     # maka big(o) (row+1) * column+1) karena ada (0,1,2,3) * (0,1,2,3) kemunginan untuk menempati 2 digit angka jadi (row * column)
    if temp in memo:
        return memo[temp]
    if temp == "1*1":
        return 1
    memo[temp] = GridTraveler(row-1, column) + GridTraveler(row, column-1) #kalau ke bawah maka row-1 dan kalau kekanan column -1
    print(memo)
    return memo[temp]

print(GridTraveler(3, 3))

    