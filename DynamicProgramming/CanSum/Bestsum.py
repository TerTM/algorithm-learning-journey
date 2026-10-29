#bestSum mengambil array sum dengan size/length terkecil 
def bestSum(target, numbers):
    if target == 0: return []
    if target < 0: return None
    shortest_combination = None
    for i in numbers:
        remainder_combination = bestSum(target - i, numbers)
        if remainder_combination != None:
            current_combination = remainder_combination + [i] # m 
            if shortest_combination == None or len(shortest_combination) > len(current_combination):
                shortest_combination = current_combination
    return shortest_combination

#Bruteforce 
# M : target
# N : length numbers
# Time : O(n^m * m)
# Space : O(m*m)

def bestSum(target, numbers, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0: return []
    if target < 0: return None
    shortest_combination = None
    for i in numbers:
        remainder_combination = bestSum(target - i, numbers, memo)
        if remainder_combination != None:
            current_combination = remainder_combination + [i] # m 
            if shortest_combination == None or len(shortest_combination) > len(current_combination):
                shortest_combination = current_combination
    memo[target] = shortest_combination
    return shortest_combination
memo = {}
print(bestSum(8, [2,3,5], memo))
print(memo)
# memo = {}
# print(bestSum(100, [1,2,3,5, 25], memo))
# print(memo)

# Time : O(m*n * m)
# Space : O(m*m)
# m pertama dari recurssion stack depth dan m selanjutnya dari operasi array