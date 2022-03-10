# 题意：如果O四个方向被X包围，就翻转； modify board in-place
# 思路：
# 1 把外围的O全部放入queue中，然后改写成A
# 2 把queue中所有元素BFS后，联通的都改写成A
# 3 把所有的A都写回O，把O都写成X
# 时间复杂度：O(n×m)
# 空间复杂度：O(n×m)
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        n, m = len(board), len(board[0])
        q = collections.deque()
        for i in range(n):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "A"
            if board[i][m - 1] == "O":
                q.append((i, m - 1))
                board[i][m - 1] = "A"
        for i in range(m - 1):
            if board[0][i] == "O":
                q.append((0, i))
                board[0][i] = "A"
            if board[n - 1][i] == "O":
                q.append((n - 1, i))
                board[n - 1][i] = "A"

        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                mx = x + dx
                my = y + dy
                if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
                    q.append((mx, my))
                    board[mx][my] = "A"

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


