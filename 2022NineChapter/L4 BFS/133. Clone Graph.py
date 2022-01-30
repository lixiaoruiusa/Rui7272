"""
# Time Complexity : O(N + M), N is a number of nodes (vertices) and M is a number of edges.
# Space Complexity : O(N)
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        queue = collections.deque([node])
        visited[node] = Node(node.val, [])

        # BFS
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[current_node].neighbors.append(visited[neighbor])
        return visited[node]

