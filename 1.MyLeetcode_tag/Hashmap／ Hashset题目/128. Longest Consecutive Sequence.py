"""
题意：找最长的连续Sequence  Input: nums = [100,4,200,1,3,2] Output: 4
思路：input去重，loop num，检查num的上下游， 用dic来记录num是否访问过，从而优化到O(n).
O(n) time | O(n) space
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = list(set(nums))
        dic = {}
        res = 1
        for num in nums:
            dic[num] = False

        for i, num in enumerate(nums):
            if dic[num] == False:
                count = 1
                left_num = num - 1
                right_num = num + 1
                while left_num in dic:
                    dic[left_num] = True
                    count += 1
                    left_num -= 1
                while right_num in dic:
                    dic[right_num] = True
                    count += 1
                    right_num += 1
            res = max(res, count)
        return res


