class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    @row: i // total columns
    @col: i % total columns
    @ Time O(log(m*n))  Space O(1)
    """
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        total_row = len(matrix)
        total_col = len(matrix[0])
        start = 0
        end = total_row*total_col - 1 
        while start + 1 < end:
            mid = (start + end) // 2
            row = mid // total_col
            col = mid % total_col
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid
            else:
                end = mid
        row = end // total_col
        col = end % total_col
        if matrix[row][col] == target:
            return True
        row = start // total_col
        col = start % total_col
        if matrix[row][col] == target:
            return True
        return False    