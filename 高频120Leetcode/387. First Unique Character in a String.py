class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}

        for ch in s:
            if ch not in dic:
                dic[ch] = 1
            else:
                dic[ch] += 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1

# 用Counter试试