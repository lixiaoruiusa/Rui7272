# Time O(n^2)
# Space O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:

        if not s:
            return 0

        count = 0
        for i in range(len(s)):
            count1 = self.count_palindrom(i, i, s)
            count2 = self.count_palindrom(i, i + 1, s)
            count = count + count1 + count2
        return count

    def count_palindrom(self, i, j, s):
        cnt = 0
        while i >= 0 and j < len(s) and s[i] == s[j]:
            cnt += 1
            i -= 1
            j += 1
        return cnt


