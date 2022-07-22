# 题意：能组成Longest Palindrome的长度是多少
# 思路：
# 有pair就+2
# 偶数个相同元素能组成，奇数个最多有1个。用set记录add和remove记录pair，remove时res+2，如果set中有剩余，res+1
# Time：O(n)
# Space：O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:

        if not s:
            return
        validate = set()
        res = 0
        for ch in s:
            if ch not in validate:
                validate.add(ch)
            else:
                validate.remove(ch)
                res += 2
        if validate:
            res += 1
        return res


