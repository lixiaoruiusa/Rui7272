# 题意：返回第Nth丑数的值， eg n = 10 return 12 注释 [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
# 思路：二刷
# 其实难点时如何生成丑数，所有的丑数都是之前的丑数 乘以了 2 3 5
# 从1开始生成丑数(current * 2, current * 3, current * 5)
# 用set记录是否遇到过，把每次的3个丑数然后放入heap中，每次heap只pop一个数，
# 所以for i in range(n)，current_ugly就是结果第nth


# Time: O(nlogn)
# Space: O(n)

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:

        heap = [1]
        visited = set([1])

        for i in range(n):
            current_ugly = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                new_ugly = current_ugly * factor
                if new_ugly not in visited:
                    heapq.heappush(heap, new_ugly)
                    visited.add(new_ugly)
        return current_ugly
