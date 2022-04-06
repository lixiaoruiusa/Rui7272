directions = [(-1, -2), (1, -2), (-2, -1), (2, -1)]

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    # Time O(n^2)
    # space O(mn)
    """

    def shortestPath2(self, grid):
        if not grid and not grid[0]:
            return -1

        row = len(grid)
        col = len(grid[0])
        dp = [[float("inf") for _ in range(col)] for _ in range(row)]
        dp[0][0] = 0

        for j in range(1, col):
            for i in range(row):
                if grid[i][j] == 1:
                    continue

                for _x, _y in directions:
                    x = _x + i
                    y = _y + j
                    if 0 <= x < row and 0 <= y < col:
                        dp[i][j] = min(dp[i][j], dp[x][y] + 1)

        if dp[-1][-1] != float("inf"):
            return dp[-1][-1]
        return -1
# 优化
    # Time O(n^2)
    # space O(3n) = O(n)
    def shortestPath2(self, grid):
        if not grid and not grid[0]:
            return -1

        row = len(grid)
        col = len(grid[0])
        dp = [[float("inf") for _ in range(3)] for _ in range(row)]
        dp[0][0] = 0

        for j in range(1, col):
            for i in range(row):
                # 清除重置滚动数组中的值恢复为 inf， 因为之前被使用了
                dp[i][j % 3] = float("inf")
                if grid[i][j] == 1:
                    continue

                for _x, _y in directions:
                    x = _x + i
                    y = _y + j
                    if 0 <= x < row and 0 <= y < col:
                        dp[i][j % 3] = min(dp[i][j % 3], dp[x][y % 3] + 1)

        if dp[row - 1][(col - 1) % 3] != float("inf"):
            return dp[row - 1][(col - 1) % 3]
        return -1
