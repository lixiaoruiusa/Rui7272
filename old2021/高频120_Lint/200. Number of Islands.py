class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    @ Time: O(n^^2)  Space O(1)
    @ DFS
    """

    class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:

            if not grid:
                return 0

            count = 0

            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "1":
                        self.dfs(grid, i, j)
                        count += 1

            return count

        def dfs(self, grid, i, j):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return

            grid[i][j] = "0"

            self.dfs(grid, i + 1, j)
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i, j + 1)
            self.dfs(grid, i, j - 1)


'''
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if len(grid) == 0:
            return 0
            
        row, column = len(grid), len(grid[0])
        res = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    res += 1
        return res
        
    def bfs(self, grid, i, j):
        check = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = [(i,j)]
        grid[i][j] = 0
        while len(queue) > 0:
            x, y = queue.pop()
            for dx, dy in check:
                if 0 <= dx + x < len(grid) and 0 <= dy + y < len(grid[0]) and grid[dx + x][dy + y] == 1:
                    grid[dx + x][dy + y] = 0
                    queue.append((dx + x,dy + y))
