def mergeSort(arr):
    if len(arr) > 1:
        d = len(arr)//2
        print(arr)
        l = arr[:d]
        print("left ",l)
        r = arr[d:]
        print("right ",r)
        mergeSort(l)
        mergeSort(r)

        i = j = k = 0
        print("before ", arr)
        print(l)
        print(r)
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+= 1
            else:
                arr[k] = r[j]
                j += 1
            k+=1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
        print("after ",arr)
a= [1,2,3,4,2]
mergeSort(a)
print(a)
