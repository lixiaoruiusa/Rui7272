# Time nlogn
# Space O(n + n + k) ~ O(n)
# import heapq
# class Solution:
#     def topKFrequent(self, words: List[str], k: int) -> List[str]:

#         if not words:
#             return []

#         count = {}
#         for word in words:
#             count[word] = count.get(word, 0) + 1

#         heap = []
#         for w, freq in count.items():
#             heapq.heappush(heap,(-freq, w))
#         res = []
#         for i in range(k):
#             freq, w = heapq.heappop(heap)
#             res.append(w)

#         return res

"""
在 a 和 b 之间进行全比较。
具体的，lt(a, b) 与 a < b 相同， le(a, b) 与 a <= b 相同，eq(a, b) 与 a == b 相同，ne(a, b) 与 a != b 相同，gt(a, b) 与 a > b 相同，ge(a, b)``与 ``a >= b 相同。注意这些函数可以返回任何值，无论它是否可当作布尔值
"""

# time nlog(k)
# space O(k)
class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            node = Node(word, freq)
            if len(heap) == k:
                heappushpop(heap, node)
            else:
                heappush(h, node)

        result = []
        while heap:
            result.append(heappop(heap).word)
        return result[::-1]