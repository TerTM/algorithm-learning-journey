def canSum(targetsum, numbers):
    arr = [False] * (targetsum+1)
    arr[0] = True # karena kita mau jika yang dicari targetsum, maka 0 kita buat True dengan pengandaian tidak mengambil angka apa2 untuk membuat 0
    for i in range(targetsum):
        if arr[i] == True:
            for j in numbers:
                if i+j <= targetsum:
                    arr[i+j] = True
    print(arr)
    return arr[targetsum]

print(canSum(7, [3, 4, 5]))
print(canSum(13, [5, 4]))

# M = Targetsum   N = len(Numbers)
# Time Complexity O(M*N)
# Space Complexity O(M)