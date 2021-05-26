"""Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Input: nums = [1], k = 1
Output: [1]
"""
# O(nlogn) Time | O(n) Space
# O(nlogk) if k < n, O(n) if k = n Time | O(n + k) space
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        heap = []

        for item in counts.items():
            heapq.heappush(heap, (-item[1], item[0]))

        res = []

        for i in range(k):
            count, value = heapq.heappop(heap)
            res.append(value)

        return res

# import heapq
# nums = [1,1,1,2,2,3]
# k = 2
# counts = {}
#
# for i in range(len(nums)):
#     if nums[i] in counts:
#         counts[nums[i]] += 1
#     else:
#         counts[nums[i]] = 1
#
# heap = []
# print(counts)
#
# for item in counts.items():
#     heapq.heappush(heap,(-item[1], item[0]))
# print(heap)
#
# results = []
#
# for i in range(k):
#     count, value = heapq.heappop(heap)
#     results.append(value)
#
# print(results)