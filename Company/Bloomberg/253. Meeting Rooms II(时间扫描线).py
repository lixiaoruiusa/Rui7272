# time nlog(n) because of sorting | space O(n) of meetings
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        meetings = []
        for interval in intervals:
            meetings.append([interval[0], 1])
            meetings.append([interval[1], -1])

        # meetings = sorted(meetings)
        meetings = sorted(meetings, key=lambda x: (x[0], x[1]))
        #print(meetings)

        count = 0
        running_cost = 0
        for time, cost in meetings:
            running_cost += cost
            count = max(count, running_cost)
        return count