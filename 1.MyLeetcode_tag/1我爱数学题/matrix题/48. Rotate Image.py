"""
题意：整个向右旋转90度
思路：两步： 1 上下行呼唤，（1-4行，2-3行）  2 斜对角线元素互换
Reverse on Diagonal and then Reverse Left to Right

Time: O(m) the number of cells in the matrix
Space: O(1)
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        top = 0
        bot = n - 1
        # 上下行换
        while top < bot:
            for col in range(n):
                matrix[top][col], matrix[bot][col] = matrix[bot][col], matrix[top][col]
            top += 1
            bot -= 1

        for i in range(1, n):
            for j in range(i):
                # 对角线换
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return matrix


