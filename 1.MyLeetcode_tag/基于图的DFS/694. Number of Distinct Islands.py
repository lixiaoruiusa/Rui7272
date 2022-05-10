"""
hashable ≈ immutable     可哈希 ≈ 不可变
在Python中：
list、set和dictionary 都是可改变的，比如可以通过list.append()，set.remove()，dict['key'] = value对其进行修改，所以它们都是不可哈希的；
而tuple和string是不可变的，只可以做复制或者切片等操作，所以它们就是可哈希的。
"""
"""
Time Complexity : O(M⋅N).
Space complexity : O(M⋅N)
"""



class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        islands = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_island = set()
                    self.dfs(i, j, grid, cur_island, i, j)
                    # tuple will convert the set to be hashable object
                    islands.add(tuple(cur_island))
        return len(islands)

    def dfs(self, x, y, grid, cur_island, bx, by):

        m, n = len(grid), len(grid[0])

        grid[x][y] = 0

        cur_island.add((x - bx, y - by))

        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if grid[nx][ny] == 0:
                continue
            self.dfs(nx, ny, grid, cur_island, bx, by)
