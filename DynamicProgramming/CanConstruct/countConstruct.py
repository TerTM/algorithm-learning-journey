def countConstruct(target, wordbank):
    if target == "":
        return 1
    count = 0
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            count += countConstruct(suffix, wordbank) 
    return count

print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))

def countConstruct(target, wordbank, memo = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    count = 0
    for word in wordbank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            count += countConstruct(suffix, wordbank, memo) 
    memo[target] = count
    return memo[target]

print(countConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aaaa", "aa", "aaa", "aaaaa", "aaaaaa"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))