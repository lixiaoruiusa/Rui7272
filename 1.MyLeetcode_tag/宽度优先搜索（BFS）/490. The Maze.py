# 题意：0是路 1是墙，只能横冲直撞的走，看能否到终点
# 思路：二刷：其实就是检查所有停止的点，是不是destination。所以就bfs找停止的点（见line36）
# 其实本题难在，bfs for directions的时候，keep往一个方向走, 把停止点append to queue, visited 记录stop的点
# Time complexity : O(mn)
# Space complexity : O(mn)

import collections


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        class Solution:
            def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

                if not maze:
                    return False

                a, b = start[0], start[1]
                visited = set()
                q = deque()
                q.append((a, b))
                visited.add((a, b))
                while q:
                    x, y = q.popleft()
                    if x == destination[0] and y == destination[1]:
                        return True

                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx = x + dx
                        ny = y + dy
                        while 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
                            nx += dx
                            ny += dy

                        # 找到出界的前一个点，入q
                        nx -= dx
                        ny -= dy
                        if (nx, ny) not in visited:
                            q.append((nx, ny))
                            visited.add((nx, ny))
                return False

"""
####

# 题意：0是路 1是墙，只能横冲直撞的走，看能否到终点
# 思路：其实本题巧妙在，bfs for directions的时候，keep往一个方向走, 把停止点append to queue, visite 记录stop的点
# Time complexity : O(mn)
# Space complexity : O(mn)

import collections
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        if not maze:
            return False
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(maze)
        n = len(maze[0])
        
        queue = collections.deque()
        queue.append((start[0],start[1]))
        maze[start[0]][start[1]] == "#"
        
        while queue:
            x, y = queue.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for dx,dy in directions:
                cx = x
                cy = y
                while 0 <= cx + dx < m and 0 <= cy + dy < n and maze[cx + dx][cy + dy] != 1:
                    cx += dx
                    cy += dy
                
                if maze[cx][cy] != "#":
                    queue.append((cx, cy))
                    maze[cx][cy] = "#"
                
        return False
"""