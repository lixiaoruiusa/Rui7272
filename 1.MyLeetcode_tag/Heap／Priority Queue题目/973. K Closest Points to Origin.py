# 题意： 返回距离中心最近的k个点，计算公式初中数学√(x1 - x2)2 + (y1 - y2)2
# 思路：# max heap，把最大的pop出去了，留下的就是k最小值
# O(nlogk) time，O(k) space。 Adding to/removing takes O(logk) time


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []
        # klog(k)
        for i in range(k):
            x, y = points[i]
            distance, point = math.sqrt(x ** 2 + y ** 2), points[i]
            heapq.heappush(h, (-distance, point))

        # O(nlogk)
        for i in range(k, len(points)):
            x, y = points[i]
            distance, point = math.sqrt(x ** 2 + y ** 2), points[i]
            heapq.heappushpop(h, (-distance, point))

        res = []
        while h:
            _, p = heapq.heappop(h)
            res.append(p)
        return res[::-1]

# import math
# import heapq
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#
#         if not points:
#             return []
#         heap = []
#         for i in range(k):
#             x, y = points[i]
#             distance, point = math.sqrt(x ** 2 + y ** 2), (x, y)
#             heap.append([-distance, point])
#         # O(n)
#         heapq.heapify(heap)
#         # O(nlogk)
#         for x, y in points[k:]:
#             distance, point = math.sqrt(x ** 2 + y ** 2), (x, y)
#             heapq.heappush(heap, [-distance, point])
#             heapq.heappop(heap)
#         res = []
#         for distance, point in heap:
#             res.append(point)
#         return res[::-1]

