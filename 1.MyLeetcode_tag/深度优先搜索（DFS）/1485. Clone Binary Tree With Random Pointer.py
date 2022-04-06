# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

# ???
#
#
#

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        visited = {}
        return self.dfs(root, visited)

    def dfs(self, root, visited):

        if root == None:
            return None

        if root in visited:
            return visited[root]

        cur = NodeCopy(root.val)
        visited[root] = cur  # 早入seen。最后再入就溢出了

        cur.left = self.dfs(root.left, visited)
        cur.right = self.dfs(root.right, visited)
        cur.random = self.dfs(root.random, visited)

        return cur

