class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    @ binary search
    @ 时间复杂度O(log(N))， 空间复杂度 O(1)
    """

    class Solution:
        def mySqrt(self, x: int) -> int:
            left = 0
            right = x
            while left + 1 < right:
                mid = (left + right) // 2
                if mid ** 2 > x:
                    right = mid
                else:
                    left = mid

            if right ** 2 <= x:
                return right

            return left