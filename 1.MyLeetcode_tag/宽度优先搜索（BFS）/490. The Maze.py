# 题意：0是路 1是墙，只能横冲直撞的走，看能否到终点
# 思路：其实本题难在，bfs for directions的时候，keep往一个方向走, 把停止点append to queue, visite 记录stop的点
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

        visited = set()
        queue = collections.deque()
        queue.append((start[0], start[1]))
        visited.add((start[0], start[1]))

        while queue:
            x, y = queue.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in directions:
                cx = x
                cy = y
                while 0 <= cx + dx < m and 0 <= cy + dy < n and maze[cx + dx][cy + dy] != 1:
                    cx += dx
                    cy += dy

                if (cx, cy) not in visited:
                    queue.append((cx, cy))
                    visited.add((cx, cy))

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