"""
Time complexity: O(N^2)

Space complexity: O(N^2)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        used = set()
        # 先枚举行，检查每行是否合法
        for i in range(9):
            used = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in used:
                    return False
                else:
                    used.add(board[i][j])

        # 先枚举列，检查每列是否合法
        for j in range(9):
            used = set()
            for i in range(9):
                if board[i][j] != "." and board[i][j] in used:
                    return False
                else:
                    used.add(board[i][j])

        # 每个分块的左上角的坐标为(i * 3, j * 3)
        for i in range(3):
            for j in range(3):
                used = set()
                for row in range(i * 3, i * 3 + 3):
                    for col in range(j * 3, j * 3 + 3):
                        if board[row][col] != "." and board[row][col] in used:
                            return False
                        else:
                            used.add(board[row][col])
        return True


