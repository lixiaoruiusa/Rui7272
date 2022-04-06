"""
题意： 把0所在的行和列都set为0
Time： O(mn)
思路1: 用 O(m+n)额外空间, 两遍扫matrix,第一遍用集合记录哪些行,哪些列有0;第二遍置0
思路2: 用O(1)空间, 关键思想: 用matrix第一行和第一列记录该行该列是否有0,作为标志位，matrix[i][0] = matrix[0][j] = 0;但是对于第一行,和第一列要设置一个标志位.

"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        memo1 = set()
        memo2 = set()
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    memo1.add(row)
                    memo2.add(col)

        for row in range(rows):
            for col in range(cols):
                if row in memo1:
                    matrix[row][col] = 0
                if col in memo2:
                    matrix[row][col] = 0
        return matrix


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        flag_row_0 = False
        flag_col_0 = False

        for i in range(n):
            if matrix[i][0] == 0:
                flag_col_0 = True

        for j in range(m):
            if matrix[0][j] == 0:
                flag_row_0 = True

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if flag_col_0:
            for i in range(n):
                matrix[i][0] = 0
        if flag_row_0:
            for j in range(m):
                matrix[0][j] = 0