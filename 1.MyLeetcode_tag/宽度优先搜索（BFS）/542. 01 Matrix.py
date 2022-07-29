# 题意： 返回矩阵中，每个点和0最近的距离
# 思路：二刷：这个思路确实diao，把所有0入q之后，相当于在处理剩下所有的1.因为所有的0都被visited了，所以保证与0相邻的1时最短结果。
# 1 所有0放入q中bfs
# 2 所有为0点入队列，一个个弹出，可以找到所有最短距离为1的节点，此时再一个个弹出最短距离为1的节点，可以找到所有最短距离为2的节点，循环往复.
# 3 因为用了visited，可以保证是从最小的加进来的。
# Time complexity: O(mn)
# Space complexity: O(mn)
import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]

        q = collections.deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
                    res[nx][ny] = res[x][y] + 1
        return res



