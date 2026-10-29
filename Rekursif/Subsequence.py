def f(i, sub ,arr, end):
    if i == end:
        print(sub)
        return
    # f(i+1, sub, arr, end) #Jadi reverse
    sub.append(arr[i])
    # print(f"f[{i}] {sub}")
    f(i+1, sub, arr, end) 
    sub.pop()
    # print(f"f[{i}] {sub}")
    f(i+1, sub, arr, end) #Engga reverse

arr = [3, 1, 2]         #Time complexitynya Big(n^2) dan space complexity yang bisa dilihat dari recursive tree adalah 3 karena 0,1,2 ada di axuliry stack
f(0, [], arr, 3)        

