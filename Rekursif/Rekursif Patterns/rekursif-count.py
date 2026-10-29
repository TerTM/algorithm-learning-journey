def f(i, s ,arr, sum,n):
    if s > sum: #Condition not satified 
        return 0
    if i == n:
        if s == sum:
            return 1
        return 0 #Condition not satified 

    s += arr[i]
    left = f(i+1, s, arr, sum,n) 

    s -= arr[i]
    right = f(i+1, s, arr, sum,n) 
    return left + right

arr = [1, 2, 1]        

print(f"subset yang sumnya adalah 2 ada sebanyak {f(0, 0, arr, 2,3)} kali")
