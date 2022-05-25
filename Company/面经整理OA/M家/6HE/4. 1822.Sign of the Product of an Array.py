class Solution:
    def arraySign(self, nums: List[int]) -> int:

        running_product = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            if nums[i] < 0:
                running_product *= -1

        if running_product > 0:
            return 1
        else:
            return -1