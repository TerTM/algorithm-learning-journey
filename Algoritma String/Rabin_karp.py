def rabkinkarp(text, pattern, q):
    m = len(text)
    n = len(pattern)
    t = 0
    p = 0
    h = 1

    for i in range(n-1):
        h = (h * d) % q

    for i in range(n):
        t = (d * t + ord(text[i])) % q
        p = (d * p + ord(pattern[i])) % q
    
    for i in range(m-n+1):
        if t == p:
            if text[i:i+n] == pattern:
                print("Pattern found at index [{}]".format(i))
            
        if i < m-n:
            t = (d* (t - ord(text[i]) * h) + ord(text[i+n])) % q
            if t < 0:
                t = (t+q)

d = 26
original = input("Input Original String\t: ")
pattern = input("Input Pattern String\t: ")
q = 23 #Bilangan prima
rabkinkarp(original, pattern, q)
