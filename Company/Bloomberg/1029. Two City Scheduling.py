class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        n = len(costs) // 2
        res = 0
        q = []
        for i in range(n):
            res += costs[i][0]
            heapq.heappush(q, costs[i][1] - costs[i][0])
        for i in range(n, 2 * n):
            res += costs[i][0]
            res += heapq.heappushpop(q, costs[i][1] - costs[i][0])
        return res

# 先让所有人去A城市，让第i个人去B城市的额外花销是costs[i][1] - costs[i][0]，使用优先队列找出额外花销最小的n个人，让他们去B城市


#         # Sort by a gain which company has
#         # by sending a person to city A and not to city B
#         costs.sort(key = lambda x : x[0] - x[1])

#         total = 0
#         n = len(costs) // 2
#         # To optimize the company expenses,
#         # send the first n persons to the city A
#         # and the others to the city B
#         for i in range(n):
#             total += costs[i][0] + costs[i + n][1]
#         return total
# Time O (nlogn) | Space O(1)