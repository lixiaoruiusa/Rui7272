"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    @ 扫描线，把所有的时间排序，按照开始时间升序，开始时间相同结束时间升序的方式进行排序，如果时间相同，结束时间在前，
      扫描一遍，当扫描到开始时间，就会多一个房间，当扫描到结束时间就少一个房间，这样扫描到i时候就是i时间所需要的最少的房间
      我们的房间数量要满足所有时间的需求，所以答案就是对所有时间所需要的最少房间取最大值，这样就能满足所有时间的开会需求了。why??
    @ Time(nlogn) n是会议数量; Space O(n)
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        room=[]
        #加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in intervals:
            room.append((i.start,1))
            room.append((i.end,-1))
        tmp=0
        ans=0
        #排序
        room=sorted(room)
        #扫描一遍
        for idx,cost in room:
            tmp+=cost
            ans=max(ans,tmp)
        return ans