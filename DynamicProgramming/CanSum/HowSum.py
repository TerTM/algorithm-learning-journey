#Bruteforce
# def Howsum(target, arr):
#     if target == 0: return []
#     if target < 0: return None
#     for i in arr:
#         remainderResult = Howsum(target-i, arr) 
#         if remainderResult != None:
#             remainderResult.append(i)
#             return remainderResult
#     return None

# print(Howsum(300, [7,14]))

#Memo
def Howsum(target, arr, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0: return []
    if target < 0: return None
    for i in arr:
        remainderResult = Howsum(target-i, arr, memo) 
        print(memo)
        if remainderResult != None:
            remainderResult.append(i)
            return remainderResult
    memo[target] = None
    return None
memo = {}
print(Howsum(22, [7,14], memo))
print(memo)

# brute force
# time O(n^m * m)
# space O(m)
# memoized
# time O(n*m^2) / n*m*m
# space O(m^2)
