"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# 1 初始化node 加入，mapping[node] = Node(cur.val)
# 2 遍历queue中cur的neighbor也放入mapping，  mapping[neighbor] = Node(cur.val)
# line 21: mapping {node1 (val1, [2,4]) : node1' (val1, [  ])}
# line 32: mapping {node1 (val1, [2,4]) : node1' (val1, [2'  ])
#                   node2 (val2, [1,3]) : node2' (val2, [  ])}

import collections
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        mapping = {}
        queue = collections.deque([node])

        mapping[node] = Node(node.val)

        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in mapping:
                    # add 点，建立 1：1', 加到queue
                    mapping[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # add 边, 给1'加入2' 4'
                mapping[cur].neighbors.append(mapping[neighbor])

        return mapping[node]