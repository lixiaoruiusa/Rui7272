class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        room = []
        for i in intervals:
            room.append([i[0], 1])
            room.append([i[1], -1])

        room = sorted(room)

        res = 0
        tmp = 0

        for idx, cost in room:
            tmp += cost
            res = max(res, tmp)

        return res