"""
Time Complexity: O(M×N)
Space Complexity: O(M×N)
题意：同样是只能往right和down走，和UniquePath 1 不一样的是中间有石头挡路
思路：还是先算dp第一行，第一列。并判断有无block，有block后边的为0
中间范围的石头dp[i][j] = 0
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] != 0:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = 1

        # dp第一行和第一列都填充上1，并判断有无block，有block后边的为0
        index1 = 0
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                print("222")
                index1 = i
                while index1 < n:
                    dp[index1][0] = 0
                    index1 += 1
                break
            else:
                dp[i][0] = 1

        index2 = 0
        for j in range(1, m):
            if obstacleGrid[0][j] == 1:
                index2 = j
                while index2 < m:
                    dp[0][index2] = 0
                    index2 += 1
                break
            else:
                dp[0][j] = 1

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

