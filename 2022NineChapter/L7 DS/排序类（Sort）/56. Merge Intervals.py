# 题意：Merge Intervals
# 思路：排序，res空 或 没重合的时候 append， 有重合的时候，判断更新end的最大值
# O(nlogn) time | O(n) space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res