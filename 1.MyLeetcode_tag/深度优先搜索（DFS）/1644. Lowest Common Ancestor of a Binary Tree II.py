# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
p和q不一定都在tree中
后根遍历
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res, p_exist, q_exist = self.dfs(root, p, q)

        if p_exist and q_exist:
            return res
        return None

    def dfs(self, root, p, q):

        if not root:
            return None, False, False

        left, lp, lq = self.dfs(root.left, p, q)
        right, rp, rq = self.dfs(root.right, p, q)

        p_exist = lp or rp or root.val == p.val
        q_exist = lq or rq or root.val == q.val

        if root.val == p.val:
            return root, p_exist, q_exist
        if root.val == q.val:
            return root, p_exist, q_exist

        if left and right:
            return root, p_exist, q_exist
        if left:
            return left, p_exist, q_exist
        if right:
            return right, p_exist, q_exist

        return None, p_exist, q_exist