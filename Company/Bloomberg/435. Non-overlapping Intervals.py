class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        ans = 0
        end = float('-inf')

        for i in sorted(intervals, key=lambda i: i[1]):
            if i[0] >= end:
                end = i[1]
            else:
                ans += 1

        return ans

