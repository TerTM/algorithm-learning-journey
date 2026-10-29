def bestSumTabulation(targetsum, numbers):
    arr = [None] * (targetsum+1)
    arr[0] = []
    for i in range(targetsum):
        if arr[i] != None:
            for j in numbers:
                if i+j <= targetsum:
                    temparr = arr[i] + [j]
                    if arr[i+j] is None or len(temparr) < len(arr[i+j]):
                        arr[i+j] = temparr
    print(arr)
    return(arr[targetsum])

print(bestSumTabulation(8, [2, 3, 5]))

# M = Targetsum   N = len(Numbers)
# Time Complexity O(M*N*M) # karena ada operasi penyalinan array
# Space Complexity O(M*M)

#
# if arr[i+j] == None:
#     arr[i+j] = temparr
# else: 
#     old = len(arr[i+j])
#     if len(temparr) < old:
#         arr[i+j] = temparr
