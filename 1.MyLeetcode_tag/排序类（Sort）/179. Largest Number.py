"""

[1, 20, 23, 4, 8]
"8 4 23 20 1"
"""
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
# 思路：
# 把nums里元素转化为string
# 用cmp_to_key排序（定义一个比较器比较string，排序）
# join成string的结果，


from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 把nums里元素转化为string
        nums = [str(num) for num in nums]

        # 用cmp_to_key排序
        nums.sort(key=cmp_to_key(self.compare))

        res = "".join(nums)

        # [0,0] 有"00"， 所以要去掉这种情况
        return str(int(res))

    # 比较函数 大数排在前边
    def compare(self, a, b):
        if a + b < b + a:
            return 1
        return -1
#
"""
nums.sort(key = functools.cmp_to_key(cmp), reverse = True) # 数组nums按照从“大”到“小”的顺序排列
nums.sort(key = functools.cmp_to_key(cmp), reverse = False) # 数组nums按照从“小”到“大”的顺序排列
nums.sort(key = functools.cmp_to_key(cmp)) # 不写时，默认是按照从“小”到“大”的顺序排列
所以默认时1是排在后边，-1时排在前边
"""

"""
def cmp(a, b):
    if a + b > b + a:
        return 1
    elif a + b < b + a:
        return -1
    else:
        return 0
当使用nums.sort(key = functools.cmp_to_key(cmp))调用时，将nums按照从小到大的顺序排列.

"""


