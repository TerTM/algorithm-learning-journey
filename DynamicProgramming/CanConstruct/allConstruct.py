def allConstruct(target, wordbank):
    if target == "":
        return [[]] #karena kita ingin hasilnya dalam bentuk array 2 dimensi
    
    result = []
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordbank)
            targetWays = [[word]+i for i in suffixWays]
            result.extend(targetWays)

    return result
            
print(allConstruct("abcd", ["ab", "c", "d"]))
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl", "l", "e"]))

def allConstruct(target, wordbank, memo = {}):
    if target in memo:
        return memo[target] 
    if target == "":
        return [[]] 
    
    result = []
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            suffixWays = allConstruct(suffix, wordbank, memo)
            targetWays = [[word]+i for i in suffixWays]
            result.extend(targetWays)

    memo[target] = result
    return memo[target]