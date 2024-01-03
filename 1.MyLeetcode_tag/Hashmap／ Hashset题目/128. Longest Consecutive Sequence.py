"""
题意：找最长的连续Sequence  Input: nums = [100,4,200,1,3,2] Output: 4
思路：
二刷：用字典记录访问过没有。向左向右找范围，打擂台。
O(n) time | O(n) space
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        dic = dict()
        nums = list(set(nums))
        for num in nums:
            dic[num] = False

        res = 0
        for i, num in enumerate(nums):
            if dic[num] == False:
                dic[num] = True
                left = num - 1
                right = num + 1

                while left in dic and dic[left] == False:
                    dic[left] = True
                    left -= 1

                while right in dic and dic[right] == False:
                    dic[right] = True
                    right += 1

                res = max(res, right - left - 1)
        return res



        # if not nums:
        #     return 0
        #
        # nums = list(set(nums))
        # dic = {}
        # res = 1
        # for num in nums:
        #     dic[num] = False
        #
        # for i, num in enumerate(nums):
        #     if dic[num] == False:
        #         count = 1
        #         left_num = num - 1
        #         right_num = num + 1
        #         while left_num in dic:
        #             dic[left_num] = True
        #             count += 1
        #             left_num -= 1
        #         while right_num in dic:
        #             dic[right_num] = True
        #             count += 1
        #             right_num += 1
        #     res = max(res, count)
        # return res


