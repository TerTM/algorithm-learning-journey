def badCharTable(t, p):
    pjg = len(p)
    # Populate the bad character table
    for i in range(pjg):
        if i < pjg-1:
            bc[ord(p[i])] = pjg-i-1
        else:
            bc[ord(p[i])] = pjg
    
    #Handle the characters not present in the pattern
    for i in range(len(t)):
        if bc[ord(t[i])] == None:
            bc[ord(t[i])] = pjg
        
    #Print the bad character table
    #cara pertama
    uniq = set(p)
    for i in uniq:
        print("bc[{}] = {}".format(i, bc[ord(i)]))

    #cara kedua
    #for i in range(pjg):
    #   print("bc[{}] = {}".format(p[i], bc[ord(p[i])]))
    print("bc[*] =", pjg)

def search(txt, pat):
    flag = False
    badCharTable(txt, pat)

    i = len(pat) - 1
    while i < len(txt):
        j = len(pat) - 1
        shift = i
        while j >= 0 and txt[shift] == pat[j]:
            j -= 1
            shift -= 1
        if j < 0:
            flag = True
            print("Pattern found at index [{}]".format(i- (len(pat)-1)))
            break
        i+=bc[ord(txt[i])]

    if flag != True:
        print("Pattern not found")

chars = 256
bc = [None]*chars
original = input("Input Originla String\t: ")
pattern = input("Input Pattern String\t: ")
search(original, pattern)

                  
    