"""
一共2n个人
最后是n个人再a城市，n个人再b城市，所有不能完全贪心（ab城市人数不对等）
所以就所有人都去a，然后选出一半pa - pb的最小的去b，
用个heap正好
总a 减去 top（pa - pb）
"""
# Time: O(nlogn), n is half of len(costs)
# Space: O(n)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        sum_a = 0
        heap = []
        for a, b in costs:
            sum_a += a
            heap.append(b - a)

        heapq.heapify(heap)
        for i in range(len(costs) // 2):
            cur = heapq.heappop(heap)
            sum_a += cur
        return sum_a

# 先让所有人去A城市，让第i个人去B城市的额外花销是costs[i][1] - costs[i][0]，使用优先队列找出额外花销最小的n个人，让他们去B城市
# O(1) space的解法先排序，撸一般的x[0] - x[1]， 撸后一半的x[1]

#         costs.sort(key = lambda x : x[0] - x[1])
#         total = 0
#         n = len(costs) // 2

#         for i in range(n):
#             total += costs[i][0] + costs[i + n][1]
#         return total
# Time O (nlogn) | Space O(1)