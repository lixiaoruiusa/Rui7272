# 题意：给一个string，Valid Palindrome
# 思路：两个指针，往中间扫
# Time complexity : O(n)
# Space complexity : O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s or len(s) < 2:
            return True

        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True