# 题意：给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T
"""
输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3
"""


# 思路：用sliding window，字典count元素，distinct记录unique，当distinct == k时候，打擂台结果，当distinct > k, 滑动左指针到valid位置
#      最后要判断一下，从未达到k的情况，返回len(k)
# Time complexity : O(N)
# Space complexity : O(k) ~ O(1)  k最大26
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        res = 0

        dic = {}
        distinct = 0

        left = 0
        for right in range(len(s)):

            dic[s[right]] = dic.get(s[right], 0) + 1

            if dic[s[right]] == 1:
                distinct += 1

            while distinct > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    distinct -= 1
                left += 1

            if distinct <= k:
                res = max(right - left + 1, res)

        return res