def f(i, sub ,arr, sum,n):
    if i == n:
        if sub == sum:
            print("sum dari sub : ",sub)
            return True
        return 
    
    sub += arr[i]
    if f(i+1, sub, arr, sum,n) == True:
        return True
    sub -= arr[i]
    if f(i+1, sub, arr, sum,n) == True:
        return True

arr = [1, 2, 1]        

f(0, 0, arr, 2,3)
