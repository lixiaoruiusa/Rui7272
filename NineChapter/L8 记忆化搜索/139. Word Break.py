
# Time complexity : O(n^3)
# Space complexity : O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        dp = [False for _ in range((len(s) + 1))]
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordDict:
                    if s[i:i + len(word)] == word:
                        dp[i + len(word)] = True
        return dp[-1]


