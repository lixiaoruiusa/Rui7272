# 思路： 1 先整体reverse 再reverse前k，再reverse后n-k就是结果
# O(n) time
# O(1) space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return nums

        k = k % len(nums)

        self.reverse_nums(0, len(nums) - 1, nums)
        self.reverse_nums(0, k - 1, nums)
        self.reverse_nums(k, len(nums) - 1, nums)
        return nums

    def reverse_nums(self, left, right, nums):

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
