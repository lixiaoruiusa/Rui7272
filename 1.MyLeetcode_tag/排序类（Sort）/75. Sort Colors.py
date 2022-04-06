# 题意：sort 0 1 2
# 思路: 两次patition
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        self.patition(nums, 1)
        self.patition(nums, 2)

    def patition(self, nums, k):

        left = 0
        right = len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

"""
# 一次扫描的办法， 三个指针，==0和left换（move index，left），==2和right换（move right），==1 move（index）
class Solution:
 
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1
        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1 # move to next number
            elif A[index] == 2:
                A[right], A[index] = A[index], A[right]
                right -= 1
            else:  # == 1, skip
                index += 1
"""