"""
求所有满足3sum < target的个数
Time: O(n^2)
Space: O(1)
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        if not nums or len(nums) < 3:
            return 0

        nums = sorted(nums)
        res = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    # 这1行right - left的个数全满足
                    res = res + right - left
                    left += 1
                else:
                    right -= 1
        return res