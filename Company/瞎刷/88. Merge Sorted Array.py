# 题意: Merge 两个 Sorted Array， 要求O(1)
# 思路: 双指针从后向前走， 把大的值放在 m + n - 1的位置上, 如果nums2有剩余，nums1[:n] = nums2[:n]
# O(m + n) time
# O(1) space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        if n > 0:
            nums1[:n] = nums2[:n]
