# 题意：如果O四个方向被X包围，就翻转； modify board in-place
# 思路：
# 二刷：道理是，最外圈为O的元素，与其相连的格子，才是翻不动的格子。剩下的O全部翻转为X
# 1 把外围的O全部放入queue中，然后改写成A
# 2 把queue中所有元素BFS后，联通的都改写成A
# 3 把所有的A都写回O，把O都写成X
# 时间复杂度：O(n×m)
# 空间复杂度：O(n×m)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        n = len(board)
        m = len(board[0])

        q = deque()

        # 把所有外圈的O都加入到q
        for i in range(n):
            if board[i][0] == "O":
                q.append((i, 0))
                board[i][0] = "A"

            if board[i][m - 1] == "O":
                q.append((i, m - 1))
                board[i][m - 1] = "A"

        for j in range(1, m - 1):
            if board[0][j] == "O":
                q.append((0, j))
                board[0][j] = "A"

            if board[n - 1][j] == "O":
                q.append((n - 1, j))
                board[n - 1][j] = "A"

        # BFS 边界的O，把所有相连的O的写成A
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == "O":
                    q.append((nx, ny))
                    board[nx][ny] = "A"

        # 现在所有O表示可以翻转变成X，所有A表示不能翻转变成O
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"

                elif board[i][j] == "A":
                    board[i][j] = "O"

        return board


