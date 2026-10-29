n = int(input('masukan banyak data mahasiswa \t: '))
mahasiswa = []
for i in range(n):
    temp = {}
    temp["nama"] = input("Masukkan nama : ")
    temp["NIM"] = input("Masukkan NIM : ")
    temp["nilai_tugas"] = int(input("Masukkan nilai tugas: "))
    temp["nilai_uas"] = int(input("Masukkan nilai uas: "))
    temp["nilai_uts"] = int(input("Masukkan nilai uts: "))
    temp["NA"] = 20/100 * temp["nilai_tugas"] + 0.4 * temp["nilai_uas"] +  0.4 * temp["nilai_uts"]
    mahasiswa.append(temp)
    print("=-"*15,"\nData berhasil ditambahkan\n","=-"*15)

print("\nData sebelum diurutkan")
for i in mahasiswa:
    print(f"Nama \t\t:{i["nama"]}\nNIM \t\t:{i["NIM"]}\nNilai Tugas \t:{i["nilai_tugas"]}\nNilai Uas\t:{i["nilai_uas"]}\nNilai UTS\t:{i["nilai_uts"]}\nNilai Akhir \t:{i["NA"]}")
    print("=-"*15,"\n\n","=-"*15)

for i in range(0, n):
    smallestindex = i
    for j in range(i+1, n):
        if mahasiswa[j]["NA"] > mahasiswa[smallestindex]["NA"]:
            smallestindex = j
    temp = mahasiswa[smallestindex]
    mahasiswa[smallestindex] = mahasiswa[i]
    mahasiswa[i] = temp

print("\nData setelah diurutkan")
for i in mahasiswa:
    print(f"Nama \t\t:{i["nama"]}\nNIM \t\t:{i["NIM"]}\nNilai Tugas \t:{i["nilai_tugas"]}\nNilai Uas\t:{i["nilai_uas"]}\nNilai UTS\t:{i["nilai_uts"]}\nNilai Akhir \t:{i["NA"]}")
    print("=-"*15,"\n\n","=-"*15)

