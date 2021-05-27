class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):

        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return

        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

# 1 从后往前找到最后升序的元素
# 2 指针移到 k = i - 1 的位置(last "ascending" position)
# 3 找到最接近 k 位置的值， 一定是j， 因为后边是单调递减，交换
# 4 再直接revers 剩下的后半部分

# O(n) time | O(1) space