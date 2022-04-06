# 题目：Course Schedule， Input: numCourses = 2, prerequisites = [[1,0]] Output: true
# 思路：
# 1 建indegrees和graph，要按照numCourses来建，不然会漏掉一些Courses。
# 2 loop prerequisites，更新indegrees {0: 1, 1: 0} 和graph {0: [], 1: [0]}
# 3 把indegrees value为0的node 放入queue
# 4 循环该node在graph的value，把相应的indegrees -= 1， 把indegrees == 0的入队
# 5 最后检查indegrees value是否都为0

# 时间复杂度: O(n+m)，其中 n 为课程数，m 为先修课程的要求数。这其实就是对图进行广度优先搜索的时间复杂度。
# 空间复杂度: O(n+m) 在广度优先搜索的过程中，我们需要最多 O(n) 的队列空间（迭代）进行广度优先搜索。因此总空间复杂度为 O(n+m)
"""
如果AOV网络有n个顶点，e条边，在拓扑排序的过程中，搜索入度为零的顶点所需的时间是O(n)。
在正常情况下，每个顶点进一次栈，出一次栈，所需时间O(n)。
每个顶点入度减1的运算共执行了e次。
所以总的时间复杂为O(n+e)。
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {x: [] for x in range(numCourses)}
        indegrees = {x: 0 for x in range(numCourses)}

        for out_node, in_node in prerequisites:
            indegrees[out_node] += 1
            graph[in_node].append(out_node)

        queue = collections.deque()
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in graph[cur]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)

        for v in indegrees.values():
            if v > 0:
                return []
        return res