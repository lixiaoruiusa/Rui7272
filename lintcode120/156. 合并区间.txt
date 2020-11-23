"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
 """

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    @Time : O(n log n) , Space: O(n) 
    @ res为空或者无交叉时即interval.start > res[-1].end时append;else取最后元素的max值
    """
    def merge(self, intervals):
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x.start)
        result = []
        for interval in intervals:
            if not result or interval.start > result[-1].end:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
        
        

'''
Space O(1)
class Solution2:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return intervals
        
        intervals.sort(key = lambda x : x.start)
        for i in range(len(intervals)):
            if i < len(intervals) - 1 and intervals[i].end >= intervals[i + 1].start:
                intervals[i + 1].start = intervals[i].start
                intervals[i + 1].end = max(intervals[i].end, intervals[i + 1].end)
                intervals[i] = None
        
        intervals[:] = [item for item in intervals if item]
        return intervals

#Leetcode
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals, key = lambda interval : interval[0])
        res = []
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
'''
