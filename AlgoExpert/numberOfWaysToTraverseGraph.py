'''
思路:由于在每个位置只能向下或者向右， 所以每个坐标的路径和等于上一行相同位置和上一列相同位置不同路径的总和，
状态转移方程：f[i][j] = f[i - 1][j] + f[i][j - 1];
复杂度:时间复杂度O(mn)。空间复杂度O(mn)
'''


def numberOfWaysToTraverseGraph(width, height):
    col = width
    row = height

    dp = [[1] * col] * row

    for i in range(1, row):
        for j in range(1, col):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]

