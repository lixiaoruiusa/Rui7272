"""
题意： 把0所在的行和列都改写为0
思路：
以第1行，第1列座位标记位置：
1 要检查除了第一个元素以外的行和列是否有0
2 只扫2行和2列以后的数字，把座位标记
3 最后扫一遍翻转0

# Space: O(1) 方法
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        if not matrix or not matrix[0]:
            return matrix

        # 1 要检查除了第一个元素以外的行和列是否有0
        frist_col_0 = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                frist_col_0 = True
                break
        frist_row_0 = False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                frist_row_0 = True
                break

        # 2 只扫2行和2列以后的数字，把座位标记
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3 最后扫一遍翻转0: 先翻转里边的行列，再检查第1行和第1列
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if frist_col_0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if frist_row_0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

"""

方法1：两个set分别参存i，j，再loop，i in set or j in set，matrix[i][j] = 0
# Time: O(MN)
# Space: O(M+N) rows最多M, cols最多N
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        if not matrix or not matrix[0]:
            return matrix

        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#
#         n = len(matrix)
#         m = len(matrix[0])
#
#         flag_row_0 = False
#         flag_col_0 = False
#
#         for i in range(n):
#             if matrix[i][0] == 0:
#                 flag_col_0 = True
#
#         for j in range(m):
#             if matrix[0][j] == 0:
#                 flag_row_0 = True
#
#         for i in range(1, n):
#             for j in range(1, m):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = matrix[0][j] = 0
#
#         for i in range(1, n):
#             for j in range(1, m):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
#
#         if flag_col_0:
#             for i in range(n):
#                 matrix[i][0] = 0
#         if flag_row_0:
#             for j in range(m):
#                 matrix[0][j] = 0