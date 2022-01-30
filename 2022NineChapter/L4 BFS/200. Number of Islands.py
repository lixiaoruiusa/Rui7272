
# import collections
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         islands = 0
#         visited = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1' and (i ,j) not in visited:
#                     visited.add((i ,j))
#                     self.bfs(grid, i, j ,visited)
#                     islands += 1
#         return islands
#
#     def bfs(self, grid, x, y, visited):
#         queue = deque([(x, y)])
#         while queue:
#             x, y = queue.popleft()
#             for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
#                 next_x = x + delta_x
#                 next_y = y + delta_y
#                 if not self.is_valid(grid, next_x, next_y ,visited):
#                     continue
#                 queue.append((next_x, next_y))
#                 visited.add((next_x ,next_y))
#
#     def is_valid(self, grid, x, y, visited):
#         n, m = len(grid), len(grid[0])
#         if not (0 <= x < n and 0 <= y < m):
#             return False
#         if (x ,y) in visited:
#             return False
#         return grid[x][y] == '1'


# DFS

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
# #             return 0
# #         count = 0
# #         for i in range(len(grid)):
# #             for j in range(len(grid[0])):
#                 if grid[i][j] == '1':
#                     self.dfs(grid, i, j)
#                     count += 1
#         return count
#
#     def dfs(self, grid, i, j):
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
#             return
#         grid[i][j] = '0'
#         self.dfs(grid, i + 1, j)
#         self.dfs(grid, i - 1, j)
#         self.dfs(grid, i, j + 1)
#         self.dfs(grid, i, j - 1)
