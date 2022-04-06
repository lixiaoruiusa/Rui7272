# 题意：求array中第k个最大值
# 思路：用heap，存k个值，把小的都pop出去，最后堆顶就是结果
# Time complexity : O(Nlogk).
# Space complexity : O(k) to store the heap elements.
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums:
            return

        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        return heap[0]
