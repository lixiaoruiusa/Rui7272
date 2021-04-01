class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    @Time O(n) Space O(1)
    @题目要点：不同值，position+1交换，返回 + 1 (因为返回的是len)
    """
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        position = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[position]:
                position += 1
                nums[position] = nums[i]
        return position + 1




    # leetcode
    '''
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #  in-place and O(1) extra memory
        
        if not nums:
            return 0
        
        index = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                index += 1
                nums[index] = nums[i]
        
        return index + 1
    '''