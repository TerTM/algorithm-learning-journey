def countConstruct(target, wordbank):
    arr = [0] * (len(target) + 1)
    arr[0] = 1 # indeks ke-0 1 karena kita ingin jika targetnya adalah str kosong maka take no element from wordbank, juga sebagai penanda index yang lagi dicari di target

    for i in range(len(arr)): #m
        if arr[i] != 0: #perlu diperhatikan yang ingin kita olah yang bukan 0 ( jadi bukan hanya 1 ) (jgua bisa baris ini didelete hasilnya sama karena nanti yang di + akan 0, karena kita menambahkan nilai berbasarkan posisi i sekarang)
            for j in wordbank: #n
                #slicing dari index sekarng ke sepanjang karakter di wordbank
                if target[i:i+len(j)] == j: #m
                    arr[i+len(j)] += arr[i]
    print(arr)
    return arr[len(target)]

print(countConstruct("abcdef", ["ab", "abc", "cd", 'abcd', "def"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl", "rp"]))
print(countConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aaaa", "aa", "aaa", "aaaaa", "aaaaaa"]))
# M = Targetsum   N = len(Numbers)
# Time Complexity O(M*N*M) # karena ada operasi penyalinan array
# Space Complexity O(M)

