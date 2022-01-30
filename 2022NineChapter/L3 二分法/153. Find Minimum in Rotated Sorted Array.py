# O(log N) time and O(1) space

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return

        left = 0
        right = len(nums) - 1

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])
