"""
res = []
def backtrack(path, choice_list):
    if base_case:
    res.append(path)
        return

    for choice in choice_list:
        if choice satisfies constrains:
            path.append(choice)
            backtrack(path, choice_list)
            path.remove(choice)

"""
"""
Time: 9!^9 因为每一行都是9*8*7*6...*1
Space: O(81) ~ O(1)

"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        self.dfs(board, 0, 0)
        return board

    def dfs(self, board, i, j):
        n = 9
        # 到达第n列，越界，换到下一行第0列重新开始
        if j == 9:
            return self.dfs(board, i + 1, 0)
        # 到达第m行，说明找到可行解，触发 base case
        if i == 9:
            return True
        # 如果有预设数字，不用我们穷举
        if board[i][j] != ".":
            return self.dfs(board, i, j + 1)


        for val in range(1, 10):
            # 如果遇到不合法的数字，就跳过
            if not self.isValid(board, i, j, val):
                continue
            # 添加选择
            board[i][j] = str(val)
            # 如果找到一个可行解，立即结束
            if self.dfs(board, i, j + 1):
                return True
            # 撤回选择
            board[i][j] = "."
        # 穷举完1~9，依然没有找到可行解，此路不通
        return False

    """
    # 判断行是否存在重复
    # 判断列是否存在重复
    # 判断 3 x 3 方框是否存在重复

    """

    def isValid(self, board, row, col, val):
        for i in range(9):
            if board[row][i] == str(val):
                return False
            if board[i][col] == str(val):
                return False
            # if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == str(val):
            #     return False

        for i in range(row // 3 * 3, row // 3 * 3 + 3):
            for j in range(col // 3 * 3, col // 3 * 3 + 3):
                if i != row and j != col and board[i][j] == str(val):
                    return False

        return True




        return True