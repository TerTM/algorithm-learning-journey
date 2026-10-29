

def m3(arr):
    low = 0
    high = len(arr)-1

    mid =(low+high)//2
    if arr[mid] < arr[low]:
        if arr[high] < arr[mid]:   #( high mid low )
            arr[low], arr[mid] = arr[mid], arr[low]
        elif arr[low] > arr[high]:      # (mid high low)
            arr[low], arr[high] = arr[high], arr[low]
            #else implisitnya  (mid low high)

    elif arr[mid] > arr[low]:
        if arr[high] > arr[mid]:    #(low mid high)
            arr[mid], arr[low] = arr[low], arr[mid]
        elif arr[high] > arr[low]:     #(low high mid)
            arr[high], arr[low] = arr[low], arr[high]
        #else implisitnya low > high (high low mid)

def median_of_three(arr, low, high):
    mid = (low + high) // 2

    # Urutkan ketiga nilai
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]

    # Setelah tiga langkah ini, urutannya:
    # arr[low] <= arr[mid] <= arr[high]
    arr[low], arr[mid] = arr[mid], arr[low]
    return arr[mid]  # posisi median




arr = [5, 2, 4]
m3(arr)
print(arr)

arr = [1, 6, 2]
arr = [5, 7, 4]
print(median_of_three(arr, 0, len(arr)-1))
arr = [1, 6, 9]
arr = [1, 6, 0]
m3(arr)
print(arr)

arr = [3, 5, 4]

m3(arr)
print(arr)

