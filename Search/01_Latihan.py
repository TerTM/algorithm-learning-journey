def printData():
    for i in range(len(dataBuah)):
        print(dataBuah[i]["nama"],dataBuah[i]["harga"],sep="\t")

def sorting(data):
    # Proses pengurutan secara descending berdasarkan harga
    for itteration in range(1,len(data)):
        for index in range(0,len(data)-itteration):
            if (dataBuah[index]["harga"] < dataBuah[index+1]["harga"]):
                temp               = dataBuah[index]
                dataBuah[index]    = dataBuah[index+1]
                dataBuah[index+1]  = temp

def InterpolationSearchAsc(data,cari):
    low  = 0
    high = len(data)-1
    while (low<=high) :
        mid = int(low + (((cari-data[low]["harga"]) * (high-low)) / (data[high]["harga"]-data[low]["harga"])))
        if (data[mid]["harga"]==cari):
            return mid
        elif (cari>data[mid]["harga"]):
            high = mid-1 #pencarian dilakukan ke bagian low
        else:
            low = mid+1 #pencarian dilakukan ke bagian high
        
    return -1

dataBuah = [{"nama":"Apel", "harga":10000},
            {"nama":"Berry", "harga":5000},
            {"nama":"Anggur", "harga":25500},
            {"nama":"Pear", "harga":18000},
            {"nama":"Jeruk", "harga":12000}]

print()
print("Sorting Harga Pada Data Buah")
sorting(dataBuah)
printData()

while True:
    print()
    cariBuah = int(input("Cari Buah dengan Harga\t: "))
    hasil  = InterpolationSearchAsc(dataBuah,cariBuah)
    if(hasil == -1):
        print(str(cariBuah) + " tidak ditemukan")
    else:
        print(str(cariBuah) + " ditemukan pada index ke-[" + str(hasil) + "]")
    
    ulang = input("Mencari Lagi [Y/N]: ")
    if ulang != 'Y':
        break