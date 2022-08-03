class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s and not t:
            return True

        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        dic = Counter(s)
        for ch in t:
            if ch not in dic:
                return False
            dic[ch] -= 1
            if dic[ch] < 0:
                return False
        return True