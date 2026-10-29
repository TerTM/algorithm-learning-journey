def canConstruct(target, wordbank):
    if target == "":
        return True
    for word in wordbank:
        if target.find(word) == 0: #memastikan dia ada di awal karena kita hanya ingin bandingkan yang prefixnya sama dengan word di wordbank
            suffix = target[len(word):]             
            if canConstruct(suffix, wordbank) == True:
                return True
    return False

print(canConstruct("aaab", ["a", "aab"]))


#memo
def canConstruct(target, wordbank, memo = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):]     
            if canConstruct(suffix, wordbank, memo) == True:
                memo[target] = True
                return memo[target]
    memo[target] = False
    return memo[target]

memo = {}
print(canConstruct("abc", ["a", "ab", "a"], memo))
print(memo)
# print(canConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aaaa", "aa", "aaa", "aaaaa", "aaaaaa"], memo))
# print(memo)
