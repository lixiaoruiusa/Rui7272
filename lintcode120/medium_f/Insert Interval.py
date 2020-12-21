"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    @interval分为三部分：
    左边 end < newInterval.start, 
    右边 start > newInterval.end, 
    中间是和newInterval纠缠不清的，把中间的interval合并，最后把三部分加起来
    @ Time: O(n)  Space: O(n) ?
    """

    def insert(self, intervals, newInterval):
        # write your code here
        left = []
        right = []
        start = newInterval.start
        end = newInterval.end
        for interval in intervals:
            if interval.end < newInterval.start:
                left.append(interval)
            elif interval.start > newInterval.end:
                right.append(interval)
            else:
                start = min(interval.start, start)
                end = max(interval.end, end)
        tmp = Interval(start, end)  # ???Interval
        return left + [tmp] + right
        
 