# 题意：网格中的最短路径，有墙，从0，0到m-1，n-1
# 思路：
# 1 正常分层BFS，（0，0，k）入队，
# 2 在判断nx，ny的时候，如果为墙1的时候，k-1放入q中； 其他还是为0才放
# Time Complexity: O(mn⋅K)
# Space Complexity: O(mn⋅K)
#
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        distance = 0
        q = collections.deque()
        q.append((0, 0, k))
        visited.add((0, 0, k))

        while q:
            for _ in range(len(q)):
                x, y, cur_k = q.popleft()
                if x == m - 1 and y == n - 1:
                    return distance
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            if cur_k > 0 and (nx, ny, cur_k - 1) not in visited:
                                q.append((nx, ny, cur_k - 1))
                                visited.add((nx, ny, cur_k - 1))
                        else:
                            if (nx, ny, cur_k) not in visited:
                                q.append((nx, ny, cur_k))
                                visited.add((nx, ny, cur_k))

            distance += 1
        return -1