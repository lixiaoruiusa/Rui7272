"""
Time complexity: O(n^2)
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        n = numRows
        dp = [[1 for j in range(i + 1)] for i in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        return dp