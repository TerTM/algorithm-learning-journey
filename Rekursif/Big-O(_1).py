def hitung():
    a = 6
    b = 4
    c = a+b
    print(c)

hitung()   #Constant O(1)


#Time Complexity adalah ukuran loop.
#Time Complexity untuk program ini linear - O(N)

n = int(input("input N = "))  #c0       c: constant
m = 0

for i in range(1, n+1):       #n
    m = m+2                   #c1

print("m ",m)                 

#T(N) = c0 + c1n = O(N)                       Linear

bil = int(input("Input Bilangan = "))
if (bil == 0):                  #c0
    print("Bilangan nol")       #c1
elif(bil > 1):                  #c2
    print("Bilangan positif")   #c3
else:
    for i in range(bil):        #n
        print(i)                #c4

#T(n) = c0 + c1+ c2 + c3 + c4n = O(n)          Linear