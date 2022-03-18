"""
解题思路：
1 时间扫描线法，把start为1， end为-1，放到数组中。
2 排序后，loop ，保存最大running max
注意区别, 此题必须用后者
# meetings = sorted(meetings, key = lambda x:x[0])
# [[1, 1], [13, 1], [13, -1], [15, -1]]
# meetings = sorted(meetings)
# [[1, 1], [13, -1], [13, 1], [15, -1]]

meetings = sorted(meetings, key = lambda x:(x[0], x[1]))
"""

# Time nlog(n) because of sorting | Space O(n) of meetings
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        meetings = []
        for interval in intervals:
            meetings.append([interval[0], 1])
            meetings.append([interval[1], -1])
        meetings = sorted(meetings)

        count = 0
        running_cost = 0
        for time, cost in meetings:
            running_cost += cost
            count = max(count, running_cost)
        return count