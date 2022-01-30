class Solution:
    """
    O(n) time | O(1) space
    """
    # 方法1：
    def sortColors(self, nums):
        if not nums or len(nums) < 2:
            return nums

        left = 0
        index = 0
        right = len(nums) - 1

        while index <= right:
            if nums[index] == 0:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                index += 1

            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1

    # # 方法2： return left
    # def sortColors(self, nums: List[int]) -> None:
    #     self.partition(nums, 1)
    #     self.partition(nums, 2)
    #
    # def partition(self, nums, k):
    #     left = 0
    #     right = len(nums) - 1
    #
    #     while left <= right:
    #
    #         while left <= right and nums[left] < k:
    #             left += 1
    #         while left <= right and nums[right] >= k:
    #             right -= 1
    #         if left <= right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1
    #     return left
