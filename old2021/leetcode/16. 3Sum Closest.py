class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if not nums or len(nums) < 3:
            return

        nums = sorted(nums)
        res = float('inf')

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current = nums[i] + nums[left] + nums[right]

                if current == target:
                    return current

                if abs(current - target) < abs(res - target):
                    res = current

                if current > target:
                    right -= 1

                if current < target:
                    left += 1

        return res