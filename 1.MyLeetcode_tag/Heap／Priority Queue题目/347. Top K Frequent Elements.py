# 题意: 按照高到低的频率，返回nums
# 思路: counter统计频率，[freq, num]放入最小堆，把n-k个小的值都pop出去
# 利用最小堆的属性，维持k个元素，把小的都pop出去，留下的就是topk
# Time: O(Nlogk)
# Space: O(k)

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h = []
        counter = Counter(nums)
        for num, freq in counter.items():

            heapq.heappush(h, (freq, num))

            if len(h) > k:
                heapq.heappop(h)
        res = []
        while h:
            f, num = heapq.heappop(h)
            res.append(num)
        return res[::-1]
