class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    @ DP: Time O(sw) Space O(n)
    """
    def wordBreak(self, s, wordSet):
        # write your code here
        if not s:
            return True
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordSet:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        return dp[-1]