class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        l = len(s)

        for mid in range(2 * l - 1): # or (2 * l):

            left = mid // 2
            right = left + mid % 2

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1

        return count










