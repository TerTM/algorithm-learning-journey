#Time complexity Quadratic - O(n^2)

k = 0
n = int(input("Input n = "))

for i in range(1, n+1):         #n
    for j in range(1, n+1):     #n
        k = k+1                 #c
    
print("k = ",k)

#Time complexity Cubic - O(n^3)

c = 0
n = int(input("Input n = "))

for i in range(1, n+1):
    for j in range(1, n +1):
        for k in range(1, n+1):
            c = c+1

print("c = ",c)

#Time Complexity Logaritmic - O(log n)      : Pengulangan yang berkurang setengahnya setiap iterasi
i = 1
n = int(input("n = "))

while (i<=n):
    print(i)
    i *= 2

#Time Complexity : linear logaritmic/linearitmic - O(n log n)

n = int(input("n = "))

for i in range(1, n+1): # n
    j = 1
    while (j<=n):       # log n 
        print(j, end=" ")
        j *= 2
#T(n) = O(n log n)