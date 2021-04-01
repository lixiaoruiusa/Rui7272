class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    @ dp
    @ 时间复杂度O(m*n) dp的O(n*m)和单调栈的O(n)
    @ 空间复杂度O(n*m) dp的大小
    """

    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        n, m = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):  # 每个位置上方有多少连续的1
            for j in range(m):
                if i == 0 and matrix[i][j]:
                    dp[i][j] = 1
                    continue
                if matrix[i][j]:
                    dp[i][j] = dp[i - 1][j] + 1
        ans = 0
        for i in range(n):  # 把每一行作为底找最大矩形
            ans = max(ans, self.largestRectangleArea(dp[i][:]));
        return ans

    def largestRectangleArea(self, height):
        stack = []
        height.append(0)
        Sum = 0
        i = 0
        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                tmp = stack.pop()
                if stack == []:
                    Sum = max(Sum, height[tmp] * i)
                else:
                    Sum = max(Sum, height[tmp] * (i - stack[len(stack) - 1] - 1))
                i -= 1  # 拿着右边界， 寻找左边界；
            i += 1
        return Sum