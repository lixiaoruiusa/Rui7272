"""
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""
# time O(n^2)
# space O(n^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle: return None

        dp = [[0 for _ in triangle[-1]] for _ in triangle]

        dp[0][0] = triangle[0][0]

        for i in range(0, len(triangle)):
            for j in range(0, i + 1):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min((dp[i - 1][j] + triangle[i][j]), (dp[i - 1][j - 1] + triangle[i][j]))

        print(dp)
        return min(dp[-1])

# 优化
# time O(n^2)
# space O(2n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle: return None

        dp = [[0 for _ in triangle[-1]] for _ in range(2)]
        print(dp)
        dp[0][0] = triangle[0][0]

        for i in range(0, len(triangle)):
            for j in range(0, i + 1):
                if i == 0 and j == 0:
                    continue
                elif j == 0:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] + triangle[i][j]
                elif j == i:
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + triangle[i][j]
                else:
                    dp[i % 2][j] = min((dp[(i - 1) % 2][j] + triangle[i][j]), (dp[(i - 1) % 2][j - 1] + triangle[i][j]))

        print(dp)
        return min(dp[(len(triangle) - 1) % 2])