def hai(x):
    if (x>0):
        print("Output = ", x)
        hai(x-1)             #Tail Recursive

def hai(x):
    if (x>0):
        hai(x-1)
        print("Output = ", x) #Non-Tail Recursive

def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1) #Non-Tail Recursive

print(faktorial(3))

def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n > 1:
        return Fibonacci(n-1) + Fibonacci(n-2) #Non-Tail Recursive

print(Fibonacci(3))

def gcd(x, y):  #FPB Tail Recursive
    if y == 0:
        return x
    elif y > 0:
        return gcd(y, x % y)

print(gcd(9, 6))

print("="*20)

def kali(a, b): 
    if a == 1:
        return b
    if a > 1:
        return kali(a-1,b) + b  #Non-Tail Recursive

print(kali(2,5))

print("="*20)

def reverse(n):
    if n < 10:
        print(n)
    else:
        print(int(n%10), end="")
        reverse(int(n/10))

reverse(1234)

print("="*20)

def balik(n, a = 0):
    if a == len(n):
        return ""              # basis: kembalikan string kosong
    return balik(n, a + 1) + n[a]  # hasil rekursi + huruf sekarang

print(balik("abc"))  # cba

def promo(coklat, tukar):
    print("promo : ", coklat//tukar)
    return int(coklat // tukar) 

def max_white_choco(uang, harga, tukar):
    coklat = int(uang // harga)
    if coklat >= tukar:
        return promo(coklat, tukar) + coklat
        
        
print(max_white_choco(16000, 2000, 2))




def printarr(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def generatebinarystring(n, arr, i):
    if i == n:
        print(i)
        printarr(arr, n)
        return

    arr[i] = 0
    generatebinarystring(n, arr, i+1)
    
    arr[i] = 1
    generatebinarystring(n, arr, i+1)

n = 2
arr = [None] * n
generatebinarystring(n, arr, 0)

