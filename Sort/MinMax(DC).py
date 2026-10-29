# def MinMax(arr, i ,j):
#     if i == j:
#         min = arr[i]
#         max = arr[j]
#     else:
#         if i == j-1:
#             if arr[i] < arr[j]:
#                 min = arr[i]
#                 max = arr[j]
#             else:
#                 min = arr[j]
#                 max = arr[i]
#         else:
#             k = int((i+j)/2)
#             min1, max1 = MinMax(arr, i, k)
#             min2, max2 = MinMax(arr, k+1, j)

#             if min1 < min2:
#                 min = min1
#             else:
#                 min = min2
            
#             if max1 > max2:
#                 max = max1
#             else:
#                 max = max2
#     return min, max

# n = int(input("Banyak Data\t\t: "))
# bil = []
# for i in range(n):
#     bil.append(int(input("Bilangan["+str(i)+"]\t: ")))

# print()
# min, max = MinMax(bil, 0, n-1)
# print("Nilai Min : ", min)
# print("Nilai Max : ", max)

mhs = [[321102, "Puspa", 90], [321123, "Sari", 70], [321105, "Andi", 69], [321121 , "Laras", 87], [321101, "Budi", 76], [321101, "Anton", 80], [3211106, "Kiran", 95]]
n = len(mhs)
for i in range(n):
    print(mhs[i])

def MinMax(arr, i ,j):
    if i == j:
        min = arr[i]
        max = arr[j]
    else:
        if i == j-1:
            if arr[i][2] < arr[j][2]:
                min = arr[i]
                max = arr[j]
            else:
                min = arr[j]
                max = arr[i]
        else:
            k = int((i+j)/2)
            min1, max1 = MinMax(arr, i, k)
            min2, max2 = MinMax(arr, k+1, j)

            if min1[2] < min2[2]:
                min = min1
            else:
                min = min2
            
            if max1[2] > max2[2]:
                max = max1
            else:
                max = max2
    return min, max

min, max = MinMax(mhs, 0, n-1)
for i in min:
    print(i)