
"""
时间复杂度：O(mn)其中 m和 n分别是矩阵的行数和列数
空间复杂度：O(mn)
思路：
1 把所有与海相邻的边都放入对应的q和visited
2 BFS两个q，把高的放入对应的visited
3 找两个visited的交集
"""

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def pacificAtlantic(self, matrix):
        n, m = len(matrix), len(matrix[0])
        altantic_queue, pacific_queue = deque(), deque()
        altantic_visited, pacific_visited = set(), set()

        # 边缘向中心bfs
        # 把边先扫进去
        for i in range(n):
            pacific_queue.append((i, 0))
            pacific_visited.add((i, 0))
            altantic_queue.append((i, m - 1))
            altantic_visited.add((i, m - 1))
        for j in range(m):
            pacific_queue.append((0, j))
            pacific_visited.add((0, j))
            altantic_queue.append((n - 1, j))
            altantic_visited.add((n - 1, j))
        # bfs
        self.bfs(matrix, pacific_queue, pacific_visited)
        self.bfs(matrix, altantic_queue, altantic_visited)
        # 检查哪些点都被两个bfs访问过了
        res = []
        for p in pacific_visited:
            if p in altantic_visited:
                res.append(list(p))
        return res

    def bfs(self, matrix, queue, visited):
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if self.is_valid(matrix, next_x, next_y) and (next_x, next_y) not in visited and matrix[next_x][
                    next_y] >= matrix[x][y]:
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))

    def is_valid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])


# DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
# class Solution:
#     def pacificAtlantic(self, matrix):
#         n, m = len(matrix), len(matrix[0])
#         altantic_queue, pacific_queue = deque(), deque()
#         altantic_visited, pacific_visited = set(), set()
#
#         # 边缘向中心bfs
#         # 把边先扫进去
#         for i in range(n):
#             pacific_queue.append((i, 0))
#             pacific_visited.add((i, 0))
#             altantic_queue.append((i, m - 1))
#             altantic_visited.add((i, m - 1))
#         for j in range(m):
#             pacific_queue.append((0, j))
#             pacific_visited.add((0, j))
#             altantic_queue.append((n - 1, j))
#             altantic_visited.add((n - 1, j))
#         # bfs
#         self.bfs(matrix, pacific_queue, pacific_visited)
#         self.bfs(matrix, altantic_queue, altantic_visited)
#         # 检查哪些点都被两个bfs访问过了
#         return [visited for visited in pacific_visited.intersection(altantic_visited)]
#
#     def bfs(self, matrix, queue, visited):
#         while queue:
#             x, y = queue.popleft()
#             for dx, dy in DIRECTIONS:
#                 next_x, next_y = x + dx, y + dy
#                 if not self.is_valid(matrix, next_x, next_y):
#                     continue
#                 if (next_x, next_y) in visited:
#                     continue
#                 if matrix[next_x][next_y] < matrix[x][y]:
#                     continue
#                 queue.append((next_x, next_y))
#                 visited.add((next_x, next_y))
#
#     def is_valid(self, matrix, x, y):
#         return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
