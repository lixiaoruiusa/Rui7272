"""
在 a 和 b 之间进行全比较。
具体的，lt(a, b) 与 a < b 相同， le(a, b) 与 a <= b 相同，eq(a, b) 与 a == b 相同，ne(a, b) 与 a != b 相同，gt(a, b) 与 a > b 相同，ge(a, b)``与 ``a >= b 相同。注意这些函数可以返回任何值，无论它是否可当作布尔值
"""
# 有比较器是因为会出线两个相同的情况，不能比较，例如k = 1, i, love
# time nlog(k)
# space O(n)
class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    # 自定义less than comparator
    # 正常比较freq小的在前边, 先弹出
    # freq相同时，# 字典序大的先弹出

    def __lt__(self, other):
        if self.freq == other.freq:
            # 字典序大的先弹出
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
                heappush(heap, node)

        result = []
        while heap:
            result.append(heappop(heap).word)
        return result[::-1]



"""
# 用最大堆, 正好相同的freq时，符合lexicographical order
# Time nlogn ??
# Time klogn 
# O(n) space
"""

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        if not words:
            return []

        counter = Counter(words)
        heap = []
        # 用最大堆, 正好相同的freq时，符合lexicographical order
        for key, value in counter.items():
            heap.append((-value, key))

        # O(n)
        heapq.heapify(heap)
        res = []

        # klogn
        for i in range(k):
            _, w = heapq.heappop(heap)
            res.append(w)
        return res

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