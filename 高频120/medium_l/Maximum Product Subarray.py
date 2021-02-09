class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    @ 时间复杂度O(n)枚举了数组的长度
    @ 空间复杂度O(n)消耗了等长的空间 why not O(1)??
    """

    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return None

        global_max = prev_max = prev_min = nums[0]

        for num in nums[1:]:
            if num > 0:
                curr_max = max(num, prev_max * num)
                curr_min = min(num, prev_min * num)
            else:
                curr_max = max(num, prev_min * num)
                curr_min = min(num, prev_max * num)

            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min

        return global_max
