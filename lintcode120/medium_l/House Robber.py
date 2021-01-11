class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    @ 时间复杂度 O(n)，空间复杂度 O(n)
    """

    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)

        f = [0] * len(A)
        f[0] = A[0]
        f[1] = max(A[0], A[1])

        for i in range(2, len(A)):
            f[i] = max(f[i - 1], f[i - 2] + A[i])

        return f[len(A) - 1]


    # 优化：@ 时间复杂度 O(n)，空间复杂度 O(1)
    # 因为实际上只需要记录前两个状态来算第三个状态，使用滚动数组的做法，将每个下标直接 % 3
    # for i in range(2, len(A)):
    #     f[i % 3] = max(f[(i - 1) % 3], f[(i - 2) % 3] + A[i])
    # return f[(len(A) - 1) % 3]