
 
# Sorting bubble 
# ascending
n = int(input('masukan banyak data: '))
print('-'*10)
bil = []
for i in range (n):
    bil.append(int(input('masukan angka : ')))

# print('data sebelum diurutkan')
# for i in range (n):
#     print(bil[i],end=' ')

for iter in range (0,n-1):
    for ind in range(0,n-iter-1):
        swap = 0
        if bil[ind] > bil[ind+1]:                 # (ascending order)
            temp = bil[ind]
            bil[ind] = bil[ind+1]
            bil[ind+1] = temp 
            swap = 1
    if swap == 0:
        break
print()
print('data setelah diurutkan')
for i in range (n):
    print(bil[i],end=" ")



# Sorting Selection
# asceding

n = int(input('masukan banyak : '))
print('-'*10)
bil = []
for i in range (n):
    bil.append(int(input('masukan : ')))

for i in range (n-1):   #ascending
    smallestindex = i 
    for j in range (i+1, n):
        if (bil[j] < bil[smallestindex]):  #cari yang paling kecil
            smallestindex = j
        else:
            continue
    temp = bil[i]
    bil[i] = bil[smallestindex]
    bil[smallestindex] = temp

print()
print('data udh urut')
for i in range (n):
    print(bil[i],end=" ")


# insertion selection akan menyisipkan dan menggeser elemen disebelahnya
# n = int(input('masukan banyak : '))
# print('-'*10)
# bil = []
# for i in range (n):
#     bil.append(input('masukan angka : '))

# for first in range(1, n):
#     temp = bil[first]
#     loc = first
#     while bil[loc-1] > temp and loc >= 1:
#         bil[loc] = bil[loc-1]
#         loc -=1
#     bil[loc] = temp

#sama aja
numbers = [5,3, 1,2,4]
for i in range(1, len(numbers)):
    j = i
    while j > 0 and numbers[j-1] > numbers[j]:
        temp = numbers[j-1]
        numbers[j-1] = numbers[j]
        numbers[j] = temp  
        print(numbers)
        j -=1

# print()
# print('data udh urut')
# for i in range (n):
#     print(bil[i],end=" ")

    





