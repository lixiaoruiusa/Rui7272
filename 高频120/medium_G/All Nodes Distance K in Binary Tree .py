"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import collections
class Solution:
    """
    @param root: the root of the tree
    @param target: the target
    @param K: the given K
    @return: All Nodes Distance K in Binary Tree
    @ O(n) time | O(n) space
    @   # 1. construct graph
        # 2. compute distance: BFS
    """

    def distanceK(self, root, target, K):
        if not root or not target:
            return []

        graph = collections.defaultdict(set)
        self.build_graph(root, None, graph)
        return self.bfs(graph, target.val, K)

    def build_graph(self, root, father, graph):
        if not root:
            return

        for node in [father, root.left, root.right]:
            if node:
                graph[root.val].add(node.val)

        if root.left:
            self.build_graph(root.left, root, graph)
        if root.right:
            self.build_graph(root.right, root, graph)

    def bfs(self, graph, val, k):
        queue = collections.deque([val])
        distance = {val: 0}
        ans = []

        while queue:
            node = queue.popleft()
            if distance[node] == k:
                ans.append(node)

            for neigh in graph[node]:
                if neigh in distance:
                    continue
                queue.append(neigh)
                distance[neigh] = distance[node] + 1
        return ans