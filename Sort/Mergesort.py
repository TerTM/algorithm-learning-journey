def merge(arr, low, high, mid): #Time complexity O(n log n)           Space complexity Big O(N)
    temp = []
    left = low
    right = mid+1
    while left <= mid and right <= high: #selama left atau right belom habis akan terus dibandingkan
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right +=1

    while left <= mid:
        temp.append(arr[left])
        left +=1

    while right <= high:
        temp.append(arr[right])
        right +=1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]        #karena loop langsunng dari low ke high jadi index arraynya sudah sesuai tinggal menyesuaikan index tempnya agar mulai dari 0 
    #atau bisa juga seperti ini
    # for i in range(len(temp)):
    #     arr[i+low] = temp[i]      menambahkan low sebagai dasar/penyesuai kita sedang ingin untuk merubah array di index keberapa

def mergesort(arr, low = 0, high = None):
    if high == None:        #untuk mendapaatkan default argumen dari high 
        high = len(arr)-1
    if low >= high:         #Basecase pakai > untuk jaga2 walau sebenarnya aman
        return              #Jika hanya ada satu elemen maka masuk ke base case
    mid = (low+high)//2
    mergesort(arr, low, mid)
    mergesort(arr, mid+1, high)
    merge(arr, low, high, mid)  #conquer
    print(arr)



mergesort([5,3,1,2,8])
