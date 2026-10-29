#BRuteforce technique
def stringMatch(text, pattern):

    n = len(text)
    print(n)
    m = len(pattern)
    print(m)
    for i in range(n-m+1):
        j = 0
        while j < m and text[i+j] == pattern[j]: 
            j+=1
        if j == m:
            return i
    return -1

print(f"ditemukan di indeks ke-{stringMatch("Saya Mahasiswa UBM", "siswa")}")

#Multi
def stringmatch(text, pattern, last):
    for i in range(last, len(text)-len(pattern)+1):
        j = 0
        while j < len(pattern) and text[i+j] == pattern[j]:
            j+=1
        if j == len(pattern):
            return i
        
    return -1



original = input("Input Original String: ")
pattern = input("Input Pattern String: ")
print("--------------------------")

result = -1
flag = -1
while True:
    result = stringmatch(original, pattern, result+1)    
    if result != -1:
        flag += 1
        print("Pattern ditemukan pada index [{}]".format(result))
    else:
        break