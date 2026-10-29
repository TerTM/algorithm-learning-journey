def sortedLinerSearchAsc(data,x,cari):
    for i in range(x):
        if (data[i]==cari):
            return i
        if (data[i]>cariBil):
            return -1
    
    return -1

n = int(input("Banyak Data\t: "))
print("-------------------------")
bil = []
for i in range(n):
    bil.append(int(input("Bilangan["+str(i)+"]\t: ")))

print()
cariBil = int(input("Cari Data\t: "))

hasil = sortedLinerSearchAsc(bil, n, cariBil)
if hasil == -1:
    print("Data tidak ditemukan")
else:
    print("Data ditemukan pada indeks ke-["+str(hasil)+"]")