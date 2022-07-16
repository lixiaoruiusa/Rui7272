# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

"""
1 1 1 1
1 1 1 1
1 1 1 1
0 1 0 1
0 1 0 1 
"""


# time O(nm)
# space O(nm)
def update_matrix(grid):
    if not grid or not grid[0]:
        return grid

    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i, j) not in visited:
                visited.add((i, j))
                dfs(grid, visited, i, j)
    return grid


def dfs(grid, visited, i, j):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1)：
        return
    grid[i][j] = 1
    visited.add((i, j))

    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        x = i + dx
        y = j + dy
        dfs(grid, x, y)
    return



grid = [[1,1,1],[1,0,1],[1,1,1]]








