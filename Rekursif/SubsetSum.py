#Return all the subset sum in increasing order
a = []
subset = [3, 1, 2]
def subsetsum(i,arr, sum, answer): #time complexity  2^n
    if i == len(arr):
        answer.append(sum)
        return 
    subsetsum(i+1, arr, sum+arr[i], answer)
    subsetsum(i+1, arr, sum, answer)

subsetsum(0, subset, 0, a)
a.sort() #time complexity 2*n log 2*n
print(a)
#time complexity 2^n + 2*n log 2*n 
