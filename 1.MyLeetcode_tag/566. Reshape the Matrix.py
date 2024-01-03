"""
i=x // col
j=x % col

(i,j)→i×n+j

时间复杂度：O(rc)
空间复杂度：O(1)
"""


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        matrix = [[0 for _ in range(c)] for _ in range(r)]
        for x in range(m * n):
            matrix[x // c][x % c] = mat[x // n][x % n]

        return matrix
