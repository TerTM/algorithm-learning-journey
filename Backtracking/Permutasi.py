karyawan = ["Ani", "Budi", "Cici"]

hasil = []

def backtrack(path):
    if len(path) == 2:
        hasil.append(path[:]) #karena append hanya menambahkanr referensi ke objek dan bukan membuat salinannya jadi
        return                  #kita menggunakan [:] untuk membuat salinannya secarq manual
    for nama in karyawan:
        if nama not in path:
            path.append(nama)
            backtrack(path)
            path.pop()
backtrack([])

for shift in hasil:
    print(shift)