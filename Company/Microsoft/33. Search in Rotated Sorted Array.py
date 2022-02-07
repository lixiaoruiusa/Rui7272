# 切鱼头
# Time O(logN).
# Space O(1).
# 1 if (A[mid] > A[left]): #此时left和mid肯定处在同一个递增数组上 #那么就直接运用原始的二分查找
# 2 要注意两个if中边界分别有等于情况 nums[left] <= target：   target <= nums[right]:
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