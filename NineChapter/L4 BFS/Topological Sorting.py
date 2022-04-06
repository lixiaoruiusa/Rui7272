"""
描述
给定一个有向图，图节点的拓扑排序定义如下:
对于图中的每一条有向边 A -> B , 在拓扑排序中A一定在B之前.
拓扑排序中的第一个节点可以是图中的任何一个没有其他节点指向它的节点.
针对给定的有向图找到任意一种拓扑排序的顺序.
样例 1：
输入：
graph = {0,1,2,3#1,4#2,4,5#3,4,5#4#5}
输出：
[0, 1, 2, 3, 4, 5]
"""

"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

import collections
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):

        indegrees = {}
        for x in graph:
            indegrees[x] = 0
        for x in graph:
            for node in x.neighbors:
                indegrees[node] += 1

        res = []
        queue = collections.deque()
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for node in cur.neighbors:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    queue.append(node)
        for v in indegrees:
            if indegrees[v] > 0:
                return []
        return res



