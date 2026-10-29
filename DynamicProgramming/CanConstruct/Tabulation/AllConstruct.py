def allConstruct(target, wordbank):
    arr = [[] for x in range(len(target)+1)] #Di Python 3, variabel yang dibuat di dalam List Comprehension bersifat lokal
    arr[0] = [[]] #indeks ke-0 [] karena kita ingin jika targetnya adalah str kosong maka take no element from wordbank

    for i in range(len(target)):
        if arr[i] != []:
            for j in wordbank:
                if target[i:i+len(j)] == j:
                    temp = [x+[j] for x in arr[i]] #x adalah fondasi/jalan yang sudah kita punya
                    arr[i+len(j)].extend(temp)
    return arr[len(target)]

print(allConstruct("abcdef", ["a", "ab"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", 'abcd', "def", "c", "ef"]))
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl", "rp"]))

# Di setiap langkah (setiap huruf target), kita bisa memiliki hingga N cabang pilihan.
# Karena panjang targetnya adalah M, maka kita punya struktur pohon dengan kedalaman M.
# Jumlah total kombinasi secara kasar adalah: N * N * N ... sampai M             alias N^M tanpa mempertimbangkan pengcopy an