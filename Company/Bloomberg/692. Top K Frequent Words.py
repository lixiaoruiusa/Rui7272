# O(n log k) time | O(n) space
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        if not words:
            return []

        count = {}

        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

        heap = []
        for w, freq in count.items():
            heapq.heappush(heap, (-freq, w))

        res = []
        for i in range(k):
            freq, w = heapq.heappop(heap)
            res.append(w)

        return res

