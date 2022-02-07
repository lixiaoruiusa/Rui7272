# Time complextiy : O(n)
# Space complexity: O(1)
# 若发现不同，index ++ 然后赋值 nums[j]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return

        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index + 1
