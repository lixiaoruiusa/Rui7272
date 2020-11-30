class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    @ binary search
    @ Time:O(log(n))
    @ 本题成立的条件是 m**2 <= x < (m+1)**2
    """
    def sqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                right = mid - 1
            else:
                left = mid + 1