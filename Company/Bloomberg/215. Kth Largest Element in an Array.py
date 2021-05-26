# nlog(k) time | O(k) space

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return

        heap = []

        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k):
            res = heapq.heappop(heap)

        return res * (-1)

