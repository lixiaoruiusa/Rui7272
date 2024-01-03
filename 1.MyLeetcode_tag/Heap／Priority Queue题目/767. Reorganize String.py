# 题意：重排string到没有同样的字母相邻
# 思路：
# 二刷
# 1 先counter，把[-f,c] 放入最大堆heap
# 2 每次pop两个值，append到res，更新freq在放回heap
# 3 最后len(heap) == 1 or == 0, 再更新res
# Time O(n) + O(k) + n * logk   , n is length of s, k <= 26
# Space O(n) for res, O(1) for counter and heap

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:

        counter = Counter(s)
        # 边界条件,有字母数量多于半数，无法组成不相邻
        if max(counter.values()) > (len(s) + 1) // 2:
            return ""

        h = []
        for c, f in counter.items():
            h.append([-f, c])
        heapq.heapify(h)

        res = []
        while len(h) > 1:
            f1, ch1 = heapq.heappop(h)
            f2, ch2 = heapq.heappop(h)
            res.append(ch1)
            res.append(ch2)
            f1 += 1
            f2 += 1
            if f1 != 0:
                heapq.heappush(h, [f1, ch1])
            if f2 != 0:
                heapq.heappush(h, [f2, ch2])

        if h:
            f, c = heapq.heappop(h)
            if f < -1:
                return ""
            else:
                res.append(c)
        return "".join(res)

