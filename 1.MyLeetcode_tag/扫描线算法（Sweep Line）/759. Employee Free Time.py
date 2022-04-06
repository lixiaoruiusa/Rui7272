"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# 思路：
# 把所有interval都放入intervals
# 排序，merge intervals
# 间隔的位置就是要求的结果
# Time nlogn
# Space n

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        intervals = []
        for sche in schedule:
            for s in sche:
                intervals.append([s.start, s.end])

        intervals = sorted(intervals)

        res = []
        for i in intervals:
            if not res:
                res.append(i)

            elif res[-1][1] >= i[0]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)

        results = []
        for i in range(1, len(res)):
            result = Interval(res[i - 1][1], res[i][0])
            # result.start = res[i - 1][1]
            # result.end = res[i][0]

            results.append(result)

        return results

"""
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
      
        working_time = []
        for lst in schedule:
            for time in lst:
                working_time.append([time.start, time.end])
        res = []
        working_time.sort()
        print(working_time)
        
        pre_start, pre_end = working_time[0]
        for start, end in working_time[1:]:
            # 有间隔，所以append (pre_end, start)
            if start > pre_end: 
                res.append(Interval(pre_end, start))
            # 打擂台，取最大的end作为pre_end    
            pre_end = max(end, pre_end)
        return res


"""