# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
# 思路： 定义一个比较器比较string，排序拼接


from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        nums.sort(key=cmp_to_key(self.cmp))

        res = str(int("".join(nums)))

        return res

    def cmp(self, x, y):
        if x + y < y + x:
            return 1
        return -1



