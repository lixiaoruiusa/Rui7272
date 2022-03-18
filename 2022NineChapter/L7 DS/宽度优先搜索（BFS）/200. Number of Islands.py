
"""
# BFS # Time O(MN) and Space O(min(M,N))
import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid and not grid[0]:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.bfs(grid, i, j)
        return count

    def bfs(self, grid, i, j):
        queue = collections.deque([(i, j)])
        grid[i][j] = "#"
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + dx
                next_y = y + dy
                if (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and grid[next_x][next_y] == "1"):
                    queue.append((next_x, next_y))
                    grid[next_x][next_y] = "#"
        return
# BFS
# import collections
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         if not grid and not grid[0]:
#             return 0
#
#         visited = set()
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     count += 1
#                     self.bfs(grid, i, j, visited)
#         return count
#
#     def bfs(self, grid, i, j, visited):
#         queue = collections.deque([(i, j)])
#         visited.add((i, j))
#
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
#                 next_x = x + dx
#                 next_y = y + dy
#                 # check valid
#                 if (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]) and (next_x, next_y) not in visited and
#                         grid[next_x][next_y] == "1"):
#                     queue.append((next_x, next_y))
#                     visited.add((next_x, next_y))
#         return

"""
"""
DFS # Time O(MN) and Space O(MN)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
              return 0
          count = 0
          for i in range(len(grid)):
              for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

"""
"""
# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count
    
    
    def dfs(self, grid, i, j):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1"):
            return 
        
        grid[i][j] = "#"
        
        for dx, dy in [(-1, 0),(0, -1),(1, 0),(0, 1)]:
            x = i + dx
            y = j + dy
            self.dfs(grid, x, y)
        return 
"""
"""
# DFS 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 
        
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, i, j, visited)
                    count += 1
        return count
    
    
    def dfs(self, grid, i, j, visited):
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1" and not visited[i][j]):
            return 
    
        visited[i][j] = True
            
        for dx, dy in [(-1, 0),(0, -1),(1, 0),(0, 1)]:
            x = i + dx
            y = j + dy
            self.dfs(grid, x, y, visited)
            
        return 

"""