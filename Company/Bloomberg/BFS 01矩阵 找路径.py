"""
Input in 2D:
1 0 1
1 1 1
0 1 1

Input = [[1,0,1], [1,1,1], [0,1,1]]

Output:
(0,0) (1,0) (1,1) (2,1) (2,2)
(0,0) (1,0) (1,1) (1,2) (2,2)

if impossible to reach bottom-right corner, print "No paths."
"""
import collections


def labyrinth(grid):
    n = len(grid)
    m = len(grid[0])

    if not grid or not grid[0] or grid[0][0] != 1:
        return "No paths."

    q = collections.deque()
    q.append([0, 0])
    visited = set()
    visited.add([0, 0])

    while q:
        x, y = q.popleft()
        if
