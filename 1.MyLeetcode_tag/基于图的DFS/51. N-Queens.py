"""
[['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
Time complexity: O(N!)
Space complexity: O(N^2)
"""
"""
判断isVaild要检查：
1 本列是否有Q
2 左上角是否有Q
3 右上角是否有Q
如果有一行没有走成，就backtrack到上一行

Time complexity: O(N!)
Space complexity: O(N^2)
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        self.dfs(board, 0, n, res)
        return res

    def dfs(self, board, row, n, res):
        # 如果走到最后一行，说明已经找到一个解
        if row == n:
            temp_res = []
            for temp in board:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            res.append(temp_res)

        for col in range(n):
            # if not self.isVaild(board, row, col):
            #     continue
            if self.isVaild(board, row, col):
                board[row][col] = 'Q'
                self.dfs(board, row + 1, n, res)
                board[row][col] = '.'


    def isVaild(self, board, row, col):
        # 判断同一列是否冲突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        # 判断左上角是否冲突
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True