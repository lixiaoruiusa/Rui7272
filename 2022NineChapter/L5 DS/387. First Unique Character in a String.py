# O(n) time and O(26)=O(1) space
class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1

        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
