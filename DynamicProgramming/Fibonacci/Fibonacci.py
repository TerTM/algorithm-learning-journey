#TOP Down 
fib = [0] * 10
def Topdown(n):
    if fib[n] != 0:
        return fib[n]
    if n == 1 or n == 0:
        fib[n] = n
    else:
        fib[n] = Topdown(n-1) + Topdown(n-2)
    return fib[n]

Topdown(9)
print(fib)

def memoization(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = memoization(n-2) + memoization(n-1)
    return memo[n]
    
print(memoization(10))

#Bottom UP ke 1
fib = [0] * 10
def BottomUp(n):
    if n == 0 or n == 1:
        fib[n] = n
        return n
    if fib[n] != 0:
        return fib[n]
    for i in range(2, n+1):
        fib[i] = BottomUp(i-1) + BottomUp(i-2)

BottomUp(9)
print(fib)

#Bottom Up ke 2
fib  = [0] * 10
fib[1] = 1
def BottomUp(n):
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
BottomUp(9)
print(fib)



