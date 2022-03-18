class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return

        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = row * col - 1

        while start + 1 < end:

            mid = (start + end) // 2

            if matrix[mid // col][mid % col] == target:
                return True

            elif matrix[mid // col][mid % col] > target:
                end = mid
            else:
                start = mid

        if matrix[start // col][start % col] == target or matrix[end // col][end % col] == target:
            return True

        return False







