'''
587 · 两数之和 - 不同组成
描述
给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值, 返回对数.
输入: nums = [1,1,2,45,46,46], target = 47
输出: 2
解释:

1 + 46 = 47
2 + 45 = 47
'''

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        if not nums or len(nums) < 2:
            return 0

        nums.sort()

        left = 0
        right = len(nums) - 1
        cnt = 0
        while left < right:
            if nums[left] + nums[right] == target:
                cnt += 1
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right + 1] == nums[right]:
                    right -= 1

            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return cnt
