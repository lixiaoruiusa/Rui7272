"""
题目： 给一个数组，其中必有一个数出现的次数大于等于数组长度的一半。需要找出这个数
解法： 先用了哈西表的方法，然后面试官要求把空间复杂度优化为1
"""

a = [0, 0, 0, 0, 0, 0 , 1, 1, 1, 1, 1, 2, 3]


def find_most_num(nums):
    nums = sorted(nums)
    res_num = nums[0]
    res_count = 0
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count > res_count:
            res_count = count
            res_num = nums[i]
    return res_num, res_count


res_num, res_count = find_most_num(a)
print(res_num)
print(res_count)
