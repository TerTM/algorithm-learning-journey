def InterpolationSearchAsc(data, x, cari):
    low = 0
    high= x-1
    while (low<=high):
        mid = int(low + ((cari-data[low]) * (high-low) / (data[high] - data[low])))
        if (data[mid] == cari):
            return mid
        elif (cari<data[mid]):
            high = mid-1
        else:
            low = mid - 1
    return -1

n = int(input("Banyak Data\t: "))
print("-"*15)
bil = []
for i in range(n):
    bil.append(int(input("Bilangan["+str(i)+"]\t: ")))
    
print()
cariBil = int(input("Cari Data\t: "))

hasil = InterpolationSearchAsc(bil, n, cariBil) 
if hasil == -1:
    print("Data tidak ditemukan")
else:
    print("Data ditemukan diindex ke-"+str(hasil))