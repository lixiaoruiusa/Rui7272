"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import heapq


class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    @ 即使加了快排，这个实现的时间复杂度是 O(max(n, klogk))。在k比n小很多时，比O(nlogk)的堆解要优，在k和n接近时，复杂度一样。
    @ space: O(k)
    @ Min Heap解法:
    For loop 将所有的point push到min heap
    min heap pop出k个point，即为result所需
    官方版本以及多数同学分享的都是Max Heap解法（打擂台保持K个points）:
    For loop 将所有的point push到max heap
    在这里dist取反，使之成为max heap
    通过pop保持max heap size为k
    max heap最后pop出k个points的时候，需要再reverse一下顺序
    这种取反做max heap, 最后再reverse的思路，有点像双重否定表肯定，思路转了两个弯，硬套top k系列模板个人认为不可取。 求smallest k points, 直接使用min heap思维最直接, 思维复杂度最小
    """

    # Solution1: Heap
    def kClosest(self, points, origin, k):
        # write your code here
        self.heap = []
        for point in points:
            distance = self.get_distance(point, origin)
            heapq.heappush(self.heap, (distance, point.x, point.y))

        result = []
        for i in range(k):
            dis, x, y = heapq.heappop(self.heap)
            result.append(Point(x, y))

        return result

    def get_distance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

    # sloution2: quick sort

