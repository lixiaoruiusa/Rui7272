"""
思路：每次碰见左括号，就dfs，碰见右括号就return  i 和 res
# Time Complexity: O(maxK⋅n)  k是有多少个[], n 是len of string
# Space Complexity: O(n)

"""

class Solution:
    def decodeString(self, s: str) -> str:

        return self.dfs(s,0)


    def dfs(self, s, i):
        res = ""
        multi = 0

        while i < len(s):
            if '0' <= s[i] <= '9':
                multi = multi * 10 + int(s[i])
            elif s[i] == '[':
                i, tmp = self.dfs(s, i + 1)
                res += multi * tmp
                multi = 0
            elif s[i] == ']':
                return i, res
            else:
                res += s[i]
            i += 1
        return res

