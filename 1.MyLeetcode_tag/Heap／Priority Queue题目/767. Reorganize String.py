# 题意：重排string到没有同样的字母相邻
# 思路：
# 1 所有counter 放入最大堆
# 2 初始化 prev_a, prev_b = 0, "" ，存pop出来的值
# 3 pop值，把prev_b存入res中
# 3 检查 prev_a 是否还存在if prev_a < 0， 把prev push回来
# 4 更新freq，prev_a，prev_b
# Time O(nlogn)
# Space O(n)

import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:

        res = []
        counter = Counter(S)
        # 边界条件,有字母数量多于半数，无法组成不相邻
        if max(counter.values()) > (len(S) + 1) // 2:
            return ""

        heap = []
        for ch, freq in counter.items():
            heap.append((-freq, ch))
        heapq.heapify(heap)

        prev_a, prev_b = 0, ""
        while heap:
            a, b = heapq.heappop(heap)
            res.append(b)
            if prev_a < 0:
                heapq.heappush(heap, (prev_a, prev_b))
            a += 1
            prev_a, prev_b = a, b

        return ''.join(res)


