class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    # 时间复杂度: O(nlogk) 空间复杂度: O(1)
    # O(n log Len), Len为 n 段原木中最大的长度
    # 1 木头的最大值 = min(所有原木中的最大值，所有原木总长度 / 木头目标段数)
    # 2 结果在1 到 right 中，在结果集上二分

    def woodCut(self, L, k):
        if not L:
            return 0

        left = 1
        right = min(max(L), sum(L) // k)
        if right < 1:
            return 0

        while left + 1 < right:
            mid = (left + right) // 2
            if self.count_cut(L, mid) >= k:
                left = mid
            else:
                right = mid

        if self.count_cut(L, right) >= k:
            return right
        else:
            return left

    def count_cut(self, L, mid):
        count = 0
        for num in L:
            count += (num // mid)
        return count
