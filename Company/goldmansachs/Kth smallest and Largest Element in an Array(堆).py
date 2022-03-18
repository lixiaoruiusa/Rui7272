# 题意：求array中第k个最大值
# 思路：用min_heap，存k个值，把小的都pop出去，最后堆顶就是结果
# Time complexity : O(Nlogk).
# Space complexity : O(k) to store the heap elements.

"""
求第k个最大值
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
"""


"""
# 求第k个最小值
# # 思路：用max_heap，存k个值，把小的都pop出去，最后堆顶就是结果
import heapq
def find_k_small(nums, k):

    heap = []
    for num in nums[:k]:
        heap.append(-num)
    heapq.heapify(heap)
    for num in nums[k:]:
        heapq.heappushpop(heap, -num)
    return -heap[0]

a = find_k_small(nums, k)
print(a)
"""