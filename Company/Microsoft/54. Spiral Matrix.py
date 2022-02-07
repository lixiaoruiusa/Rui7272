# O(mn) time | O(1) space

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        res = []

        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])

            if top < bottom and left < right:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return res


