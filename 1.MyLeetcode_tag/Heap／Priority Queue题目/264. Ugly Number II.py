# 题意：返回第Nth丑数的值， eg n = 10 return 12 注释 [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
# 思路：从1开始 生成丑数。用set记录是否遇到过，然后放入heap中，每次heap只pop一个数，所以current_ugly就是结果
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        heap = [1]
        seen = set([1])

        current_ugly = 1
        for i in range(n):
            current_ugly = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly = current_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return current_ugly
