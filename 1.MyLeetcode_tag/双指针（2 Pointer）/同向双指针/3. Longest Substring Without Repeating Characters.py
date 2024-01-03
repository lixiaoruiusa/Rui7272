# 题意：找最长不重复的字串
# 思路：sliding window，当while dic[s[right]] > 1，字典--，left ++，打擂台比结果
# Time complexity : Time complexity : O(n)  最多O(2n) = O(n)
# In the worst case each character will be visited twice by i and j
# Space complexity：O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        dic = {}

        left = 0
        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1

            while dic[s[right]] > 1:
                dic[s[left]] -= 1
                left += 1

            res = max(right - left + 1, res)
        return res