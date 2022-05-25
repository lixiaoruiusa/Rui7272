# 找到对同一个数字，最后一次出现的index - 第一次出现的index 差值最大
def oa2(nums: list[int]) -> int:
    cache = {}
    result = 0
    for i in range(len(nums)):
        if nums[i] in cache:
            result = max(result, i - cache[nums[i]])
        else:
            cache[nums[i]] = i
    return result

print(oa2([1,1,2,3,4,2,1]))
print(oa2([2,3,4,3]))