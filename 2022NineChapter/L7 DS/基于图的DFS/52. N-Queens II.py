# Time：O(n!)   n factorial   第一行n，第二行至少n-2， 第三行至少n-4
# space O(n)
class Solution:
    def totalNQueens(self, n: int) -> int:

        if not n: return

        self.count = 0
        grid = [["." for _ in range(n)] for _ in range(n)]

        self.dfs(grid, 0, 0, n)
        return self.count

    def dfs(self, grid, row, col, n):

        if row == n:
            self.count += 1

        for col in range(n):
            if self.isvalid(grid, row, col, n):
                grid[row][col] = "Q"
                self.dfs(grid, row + 1, col, n)
                grid[row][col] = "."

    def isvalid(self, grid, row, col, n):

        # 检查列
        for i in range(n):
            if grid[i][col] == "Q":
                return False

        # 检查左上
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if grid[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # 检查右上
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if grid[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True