class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return None
        if len(nums) < 3:
            return len(nums)

        index = 0
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                index += 1
                nums[index] = nums[i]
        return index + 1