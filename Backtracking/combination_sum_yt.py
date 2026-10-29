nums = [2,3,6,7]
k = []

def combination_sum(i,target,arr):
    if target == 0:
        k.append(arr.copy())
        return
    if i == len(nums):
        return
    
    if  nums[i] <= target: 
        arr.append(nums[i])
        combination_sum(i, target-nums[i],arr)
        arr.pop()
        combination_sum(i+1, target, arr)

combination_sum(0, 7, [])

print(k)

#Part 2 https://www.youtube.com/watch?v=G1fRTGRxXU8&t=14s  
# find candidates that sum equal to target, each candidate may only be used once, solution must not contain duplicate combination

a = []
nums = [1,1,2,2,1]
def findcombination(index, target, arr, answer, temp):
    if target == 0:
        answer.append(temp.copy())
        return
    for i in range(index,len(arr)): # i disini adalah sebagai pointer posisi index yang jika masuk ke rekursif i nya akan maju ke posisi selanjutnya
        if i > index and arr[i-1] == arr[i]:  #i > index untuk memastikan agar tidak terjadi duplikasi kombinasi, sehingga untuk posisi index tersebut tidak terjadi duplikasi
            continue
        if arr[i] > target:
            break       #apakah jika diganti dengan return selalu bisa?
        temp.append(arr[i])
        findcombination(i+1, target-arr[i], arr, answer, temp) 
        temp.pop()
        
def combination_sum2(candidates, target, answer):
    candidates.sort()
    findcombination(0, target, candidates, answer, [])

combination_sum2(nums, 5, a)
print(a)