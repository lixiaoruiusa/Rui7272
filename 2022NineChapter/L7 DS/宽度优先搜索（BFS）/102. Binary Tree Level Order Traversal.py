# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# level_length = len(queue)
# 题意： 树的层级遍历
# 思路：模板， while queue的下边建level
# Time complexity : (N)
# Space complexity : O(N)
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        queue = collections.deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)
        return res


# DFS
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        self.dfs(root, 0, res)
        return res
    
    def dfs(self, root, level, res):
        if not root:
            return []
        
        if len(res) == level: 
            res.append([])
            
        res[level].append(root.val) 
        if root.left:
            self.dfs(root.left, level + 1, res)
        if root.right:
            self.dfs(root.right, level + 1, res)
"""