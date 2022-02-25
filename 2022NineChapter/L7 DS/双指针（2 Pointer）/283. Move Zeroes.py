# 看多了总想着交换，实际上move0都是硬写
# 题意： 把所有的0移动到右边，其他元素顺序不变
# 思路：放一个yingxie位置的index，把所有不为0的位置都写过来，yingxie += 1， 最后的补0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        yingxie = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[yingxie] = nums[i]
                yingxie += 1

        for i in range(yingxie, len(nums)):
            nums[i] = 0
        return nums

        # move 0 to left
        # yingxie = len(nums) - 1
        # for i in reversed(range(len(nums))):
        #     if nums[i] != 0:
        #         nums[yingxie] = nums[i]
        #         yingxie -= 1
        # for i in reversed(range(yingxie + 1)):
        #     nums[i] = 0
        # return nums