"""
题意：headID是manager，开始往下通知。数组manager中的i是第几号员工，n是数组manager的长度，informTime是对应数组manager的通知时间
思路：
        n = 4
        headID = 0
        manager = [-1, 0, 0, 1]
        informTime = [1, 9, 0, 0]
print(graph) # {0: [1, 2], 1: [3]})


时间复杂度：O(n)，遍历了每一个结点。
空间复杂度：O(n)，使用了数组存储每一个结点。

"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        if n == 1:
            return 0

        graph = collections.defaultdict(list)
        for i in range(n):
            if i != headID:
                graph[manager[i]].append(i)

        return self.dfs(headID, informTime, graph)


    def dfs(self, node, informTime, graph):
        res = 0
        for cur in graph[node]:
            cost = informTime[node]
            res = max(res, cost + self.dfs(cur, informTime, graph))
        return res




        