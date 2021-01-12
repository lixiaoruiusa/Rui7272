"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""


class Solution:
    """
    @param points: an array of point
    @return: An integer
    @ time n^2
    """

    def maxPoints(self, points):
        # write your code here
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                if points[i].x == tx:
                    slope = 'inf'
                else:
                    slope = (points[i].y - ty) / (points[i].x - tx)

                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1

                # else:
                #     dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m