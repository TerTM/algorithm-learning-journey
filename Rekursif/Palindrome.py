def isPalindrome(word, i = 0):
    if i == len(word)//2: 
        return True
    if word[i] != word[len(word)-1-i]:
        return False
    return isPalindrome(word, i + 1)

kata = input(" : ")
print(isPalindrome(kata,0))

