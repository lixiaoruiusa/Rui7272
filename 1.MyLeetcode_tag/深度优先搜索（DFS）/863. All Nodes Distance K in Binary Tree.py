# 题意：给一个node，找距离为k的nodes，返回[]
# 思路：建图 + BFS
#
# Time Complexity: O(N)
# Space Complexity: O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        if not root or not target or K < 0:
            return []

        graph = defaultdict(set)

        # DFS 建图
        self.dfs(graph, root)

        # BFS 找结果
        res = []
        self.bfs(graph, target, K, res)

        return res

    def dfs(self, graph, root):

        if not root:
            return

        if root.left:
            graph[root].add(root.left)
            graph[root.left].add(root)
            self.dfs(graph, root.left)

        if root.right:
            graph[root].add(root.right)
            graph[root.right].add(root)
            self.dfs(graph, root.right)

    def bfs(self, graph, target, K, res):

        distance = 0
        visited = set()

        queue = collections.deque([target])
        visited.add(target)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if distance == K:
                    res.append(node.val)
                    continue
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1