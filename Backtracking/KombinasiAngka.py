def combination_sum(nums, target):
    nums = sorted(nums)
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        for i in range(start, len(nums)):
            val = nums[i]
            if val > remaining:
                break
            path.append(val)
            backtrack(i, remaining - val)
            path.pop()

    backtrack(0, target)
    return result

print("Kombinasi sum untuk [2, 1], target = 2 : ")
print(combination_sum([2,3], 5))

