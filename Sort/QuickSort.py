#Time complexity O(n log n) if pivot was good           Space complexity Big O(1)

def median_of_three(arr, low, high):
    mid = (low + high) // 2

    # Urutkan ketiga nilai
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[mid] > arr[high]:
        arr[mid], arr[high] = arr[high], arr[mid]
    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]

    arr[low], arr[mid] = arr[mid], arr[low]
    return arr[mid]

def partition(arr, low, high):
    pivot = arr[low]        #Metode ambil pivot dari yang pertama

    # pivot = median_of_three(arr, low, high) msh salah

    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i < high: #cari yang lebih besar dari i
            i += 1
        while arr[j] > pivot and j > low: #cari yang lebih kecil dari j
            j -= 1
        if i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[low] #pivot
    arr[low] = arr[j]
    arr[j] = temp
    print(arr)
    return j

def quickSort(arr, low, high):
    if low < high:
        pIndex = partition(arr, low, high) 
        quickSort(arr, low, pIndex-1)
        quickSort(arr, pIndex+1, high)

a = [ 4, 6, 2, 5, 7, 9, 1, 3]

quickSort(a, 0, len(a)-1)
print(a)