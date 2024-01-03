# 题意：找左上到右下的最短路径
# 思路： 直接BFS
# Time complexity : O(mn)  the number of cells in the grid.
# Space complexity : O(mn)

import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # conner case此题比较重要
        if not grid or not grid[0] or grid[0][0] == 1:
            return -1

        m = len(grid)
        n = len(grid[0])

        distance = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        visited = set()
        q = collections.deque()
        q.append((0, 0))
        visited.add((0, 0))
        while q:
            distance += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                if x == m - 1 and y == n - 1 and grid[x][y] == 0:
                    print(grid[x][y], (x, y))
                    return distance
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
        return -1

