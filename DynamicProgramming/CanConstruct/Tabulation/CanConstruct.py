def canConstruct(target, wordbank):
    arr = [False] * (len(target) + 1) 
    arr[0] = True # indeks ke-0 True karena kita ingin jika targetnya adalah kosong maka take no element from wordbank, juga sebagai penanda index yang lagi dicari di target

    for i in range(len(arr)):
        if arr[i] == True:
            for j in wordbank:
                # Mengecek apakah target, DIMULAI DARI index 'i', diawali dengan kata 'j'
                if target.startswith(j, i):
                    arr[i+len(j)] = True
    print(arr)
    return arr[len(target)]

print(canConstruct("abcdef", ["ab", "abc", "cd", 'abcd', "def"]))

def canConstruct(target, wordbank):
    arr = [False] * (len(target) + 1)
    arr[0] = True # indeks ke-0 True karena kita ingin jika targetnya adalah kosong maka take no element from wordbank, juga sebagai penanda index yang lagi dicari di target

    for i in range(len(arr)): #m
        if arr[i] == True:
            for j in wordbank: #n
                if target[i:i+len(j)] == j: #m
                    arr[i+len(j)] = True
    print(arr)
    return arr[len(target)]

print(canConstruct("abcdef", ["ab", "abc", "cd", 'abcd', "def"]))

# M = Targetsum   N = len(Numbers)
# Time Complexity O(M*N*M) # karena ada operasi penyalinan array
# Space Complexity O(M)



    
