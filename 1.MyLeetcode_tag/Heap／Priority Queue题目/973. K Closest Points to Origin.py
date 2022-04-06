# 题意： 返回距离中心最近的k个点，计算公式初中数学√(x1 - x2)2 + (y1 - y2)2
# 思路： 所有[distance, point]放入heap中（最小堆），循环k逐个放入结果。
Time: nlogn
Space：O(n)
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if not points:
            return []

        results = []
        heap = []
        for x, y in points:
            distance, point = math.sqrt(x ** 2 + y ** 2), (x, y)
            heapq.heappush(heap,[distance, point])

        for i in range(k):
            distance, result = heapq.heappop(heap)
            results.append(result)
        return results

# 优化版可以到 O(nlogk) time，O(k) space。 Adding to/removing takes O(logk) time
# 方法：把前k个数放入max_keap中，K到后边的数逐个比较heappushpop，维持heap space 最大k+1 space
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if not points:
            return []
        heap = []
        for i in range(k):
            x, y = points[i]
            distance, point = math.sqrt(x ** 2 + y ** 2), (x, y)
            heap.append([-distance, point])
        # O(n)
        heapq.heapify(heap)
        # O(nlogk)
        for x, y in points[k:]:
            distance, point = math.sqrt(x ** 2 + y ** 2), (x, y)
            heapq.heappush(heap, [-distance, point])
            heapq.heappop(heap)
        res = []
        for distance, point in heap:
            res.append(point)
        return res[::-1]

