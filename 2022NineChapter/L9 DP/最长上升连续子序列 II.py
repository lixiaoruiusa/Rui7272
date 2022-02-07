"""
输入:
    [
      [1, 2, 3, 4, 5],
      [16,17,24,23,6],
      [15,18,25,22,7],
      [14,19,20,21,8],
      [13,12,11,10,9]
    ]
输出: 25
解释: 1 -> 2 -> 3 -> 4 -> 5 -> ... -> 25 (由外向内螺旋)
# 解题步骤：1 建 points list,存[matrix[i][j], i, j]
          2 sort points list 由小到大
          3 longest_hash {} 存 {(x,y): 1}
          4 偏移量中有： 在界内，在以前字典内，小于当前值points[i][0]的matrix[x][y]， 存longest_hash[key], longest_hash[(x, y)] + 1的最大值
          5 return max(longest_hash.values())
"""


class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """

    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        points = []
        for i in range(row):
            for j in range(col):
                points.append([matrix[i][j], i, j])
        points.sort()

        longest_hash = {}

        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            longest_hash[key] = 1

            for _x, _y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x = _x + points[i][1]
                y = _y + points[i][2]
                if 0 <= x < row and 0 <= y < col and (x, y) in longest_hash and matrix[x][y] < points[i][0]:
                    longest_hash[key] = max(longest_hash[key], longest_hash[(x, y)] + 1)
        return max(longest_hash.values())
