# 看多了总想着交换，实际上move0都是硬写
# 题意： 把所有的0移动到右边，其他元素顺序不变
# 思路：二刷
# 双指针，把right不为0的数都swap，left + 1
# 其实就是把不为0的数字都放前边来
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 双指针，把right不为0的数都swap，left + 1
        # 其实就是把不为0的数字都放前边来
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right], nums[left],
                left += 1
        return nums