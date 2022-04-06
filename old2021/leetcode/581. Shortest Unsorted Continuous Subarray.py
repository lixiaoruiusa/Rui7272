class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0

        unsorted_min = float('inf')
        unsorted_max = float('-inf')

        for i in range(len(nums)):
            if self.is_unsorted(i, nums):
                unsorted_min = min(unsorted_min, nums[i])
                unsorted_max = max(unsorted_max, nums[i])

        if unsorted_min == float('inf') or unsorted_max == float('-inf'):
            return 0

        left = 0
        right = len(nums) - 1
        while unsorted_min >= nums[left]:
            left += 1
        while unsorted_max <= nums[right]:
            right -= 1

        return right - left + 1

    def is_unsorted(self, i, nums):

        if i == 0:
            return nums[i] > nums[i + 1]

        if i == len(nums) - 1:
            return nums[i] < nums[i - 1]

        return nums[i] > nums[i + 1] or nums[i] < nums[i - 1]