class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    @ time: O(n) Space:O(1)
    """
    def maxSubArray(self, nums):
        # greedy
        '''
        if not nums:
            return 0
        
        cur_sum = max_sum = nums[0] # 初始值 设为列表第一元素
        
        for i in range(1,len(nums)):
            cur_sum = max(nums[i], cur_sum + nums[i])  # 若当前指针所指元素<0， 则丢弃之前的数列
            max_sum = max(cur_sum, max_sum) # 将当前值与最大值比较，取最大
        return max_sum
        '''
        
        #DP
        if not nums:
            return 0

        for i in range(1,len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
                
        return max(nums)
        