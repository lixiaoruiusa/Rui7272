
def max_distance(nums):
    memo = {}
    res = 0
    for i in range(len(nums)):
        if nums[i] in memo:
            res = max(res, i - memo[nums[i]])
        else:
            memo[nums[i]] = i
    return res

print(max_distance([1,1,2,3,4,2,1]))
print(max_distance([2,3,4,3]))