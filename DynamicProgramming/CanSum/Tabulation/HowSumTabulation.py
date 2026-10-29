def Howsum(targetsum, numbers):
    arr = [None] * (targetsum+1)
    arr[0] = []
    for i in range(targetsum):
        if arr[i] is not None:
            for j in numbers:
                if i+j <= targetsum:
                    arr[i+j] = arr[i] + [j] # KITA TIDAK MENGGUNAKAN APPEND KARENA FUNCTION APPEND LANGSUNG MENAMBAHKAN KE VARIABEL 
                                        # sementara kita ingin nilainya berupa return value karena kita ingin gabungkan dengan nilai arr[i] 
                                
    print(arr)
    return arr[targetsum]

# M = Targetsum   N = len(Numbers)
# Time Complexity O(M*N*M) # karena ada operasi penyalinan array
# Space Complexity O(M*M)

