# 题意：找s中最长回文Substring
# 思路：
# Expand Around Center中心线拓展法，# odd like aba， # even like abba
# get_palindrome(s, i, i) 和 get_palindrome(s, i, i + 1)
# 打擂台，求最长
# Time complexity : O(n^2)
# Space complexity : O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return

        res = ""
        for i in range(len(s)):

            res_odd = self.get_palindrome(s, i, i)
            if len(res_odd) > len(res):
                res = res_odd

            res_even = self.get_palindrome(s, i, i + 1)
            if len(res_even) > len(res):
                res = res_even
        return res

    def get_palindrome(self, s, left, right):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]