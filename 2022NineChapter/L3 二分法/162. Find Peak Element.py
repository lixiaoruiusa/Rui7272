# O(log(n)) time and O(1) space
# 二分法比较mid左右的上升下降趋势
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if not nums:
            return

        if len(nums) < 2:
            return 0

        left = 0
        right = len(nums) - 1

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid - 1]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
            else:
                return mid

        if nums[left] >= nums[right]:
            return left
        else:
            return right
