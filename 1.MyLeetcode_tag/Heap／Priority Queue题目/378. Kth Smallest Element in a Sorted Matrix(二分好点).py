"""
# 思路：
1 二分法找小于等于mid的数有多少，如果数量少于 k，那么说明最终答案不在left part。
2 get_num_less_equal
初始位置在 matrix[n - 1][0]matrix[n−1][0]（即左下角）；
设当前位置为 matrix[i][j。若matrix[i][j]≤mid，则将当前所在列的不大于 mid 的数的数量（i+1）累加到答案中，并向右移动，否则向上移动；
不断移动直到走出格子为止。
count += j + 1 是竖着一列的数量
"""

# 时间复杂度：O(nlog(r−l))，二分查找进行次数为 O(log(r−l))，每次操作时间复杂度为 O(n)
# 空间复杂度：O(1)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        if not matrix or not matrix[0]:
            return

        left, right = matrix[0][0], matrix[-1][-1]

        while left + 1 < right:
            mid = (left + right) // 2
            if self.get_num_less_equal(matrix, mid) < k:
                left = mid
            else:
                right = mid
        # 停在left和right，肯定先检查左边(因为左边可能已经满足，右边更多)
        if self.get_num_less_equal(matrix, left) >= k:
            return left
        return right

    def get_num_less_equal(self, matrix, mid):
        # 从第一行往下找，所以i，j 在右上角
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n - 1
        count = 0
        while i < m and j >= 0:
            if matrix[i][j] <= mid:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count

# 二刷，方法2：
# 这题不是往heap里放所有的，而是类似于merge多个数组的方法
# time O(n) + klogn  n is len(matrix)
# k 在最坏情况下是 n^2, 上限是n^2 log n
# space O(n) for heap

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return

        h = []
        for i in range(len(matrix)):
            h.append((matrix[i][0], i, 0))

        # O(k)
        heapq.heapify(h)

        # O k(logk)
        for i in range(k):
            res, row, col = heapq.heappop(h)
            if col == len(matrix[row]) - 1:
                continue
            heapq.heappush(h, (matrix[row][col + 1], row, col + 1))

        return res
