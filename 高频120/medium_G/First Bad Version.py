class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    @ 时间复杂度 O(nlogn) 二分的时间复杂度
    @ 空间复杂度 O(1) 无需额外空间
    """

    def findFirstBadVersion(self, n):
        # write your code here
        start = 1
        end = n
        while start + 1 < end:
            mid = (start + end) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start
        else:
            return end