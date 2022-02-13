# O(n**2) time | O(1) space
class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        for i in range(len(s)):

            # odd like aba
            cur = self.get_palindrome(s, i, i)
            if len(cur) > len(res):
                res = cur
            # even like abba
            cur = self.get_palindrome(s, i, i + 1)
            if len(cur) > len(res):
                res = cur
        return res

    def get_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]


class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        for i in range(len(s)):
            l, r = self.get_palindrome(s, i, i)
            cur = s[l: r + 1]
            if len(cur) > len(res):
                res = cur
            l, r = self.get_palindrome(s, i, i + 1)
            cur = s[l: r + 1]
            if len(cur) > len(res):
                res = cur

        return res

    def get_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1