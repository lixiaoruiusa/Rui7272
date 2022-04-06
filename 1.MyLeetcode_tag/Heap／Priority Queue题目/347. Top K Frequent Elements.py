# 题意: 按照高到低的频率，返回nums
# 思路: counter统计频率，[freq, num]放入最小堆，把n-k个小的值都pop出去
# Time: O(Nlogk)
# Space: O(k)

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        counter = Counter(nums)
        for num in counter:
            freq = counter[num]
            heapq.heappush(heap, [freq, num])
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        return res[::-1]

# 题意: 按照高到低的频率，返回nums
# 思路: counter统计频率，[-freq, num]放入最大堆，循环k，提取结果。
# Time: O(NlogN)
# Space: O(N+k)    N is for counter, k is element in heap
# import heapq
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         heap = []
#         counter = Counter(nums)
#         for num in counter:
#             freq = counter[num]
#             heapq.heappush(heap, [-freq, num])

#         res = []
#         for i in range(k):
#             neg_freq, num = heapq.heappop(heap)
#             res.append(num)
#         return res