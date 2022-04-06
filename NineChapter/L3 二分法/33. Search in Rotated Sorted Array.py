# 切鱼头 切2次鱼中段
# Time O(logN).
# Space O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1


"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left + 1 < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left =mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target: return left
        if nums[right] == target: return right
        return -1
        
"""