"""
时间复杂度：addNum: O(log n)，其中 n 为累计添加的数的数量。
          findMedian: O(1)
空间复杂度： O(n)， space of heap
# 左边 max_heap = [] # smaller
# 右边 min_heap = [] # bigger
# addNum：先往相反的方向仍num，然后把最小或者最大的丢到另一边（这样保证了左边small，右边big）
# findMedian： 如果左边长，返回-max_heap顶点；如果相等返回 （-max_heap顶点 + min_heap顶点） / 2
"""

import heapq
class MedianFinder:
    def __init__(self):

        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, - heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, - num)
            heapq.heappush(self.min_heap, - heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (- self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return - self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()