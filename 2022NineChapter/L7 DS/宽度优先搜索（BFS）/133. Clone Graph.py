"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# 题意：克隆图
# 思路：BFS的方法
# 1 字典visited记录走过的node，key为original node，val为 new node
# 2 第一个node入queue，存入visited， Node(node.val), neighbors暂时为空
# 3 loop 第一个node的neighbor，把不在visited里的neighbor存入并 建立val
# 4 同时，把对应关系的新node也存入这个neighbors里
# 返回visited[node]

# 时间复杂度：O(N) 其中 N 表示节点数量
# 空间复杂度：O(N) 哈希表使用 O(N) 的空间。

import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        visited = {}
        queue = collections.deque([node])
        visited[node] = Node(node.val)
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[cur].neighbors.append(visited[neighbor])
        return visited[node]



"""
import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        visited = {}
        queue = collections.deque([node])
        #visited[node] = Node(node.val)
        while queue:
            cur = queue.popleft()
            if cur not in visited:
                visited[node] = Node(cur.val)
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[cur].neighbors.append(visited[neighbor])
        return visited[node]
"""