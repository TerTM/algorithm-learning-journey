import time
def Cansum(target, arr):
    if target == 0:
        return True
    elif target < 0:
        return False
    for i in arr:
        if Cansum(target-i, arr) == True:
            return True
    return False

start_time = time.perf_counter()
print(Cansum(300, [7,14]))
end_time = time.perf_counter()
execution_time = end_time - start_time
print(execution_time)

#Memo agar jika sudah tau cabangnya false maka tidak perlu diteruskan lagi
memo = {}
def Cansum(target, arr, memo={}): #Big(O) time complexity target * len(arr) atau m * n sementara space O(M)
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    elif target < 0:
        return False
    for i in arr:
        if Cansum(target-i, arr, memo) == True:
            memo[target] = True
            return True
    memo[target] = False 
    return False

start_time = time.perf_counter()
print(Cansum(300, [7,14], memo))
end_time = time.perf_counter()
execution_time = end_time - start_time
print(execution_time)
print(memo)
