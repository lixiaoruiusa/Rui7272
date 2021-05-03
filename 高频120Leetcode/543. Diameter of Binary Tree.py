# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root: return 0

        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)

        res = max(res, left + right)

        return max(left, right) + 1
