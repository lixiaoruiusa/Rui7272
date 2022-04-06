# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p or root.val == q:
            return root

        # p, q 都在左子树
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # p, q 都在右子树
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # p, q 分别在左右子树，那么root即为结果
        return root


# coner case root = p or q
# p, q 都在左子树, 左递归
# p, q 都在右子树， 右递归
# p, q 分别在左右子树，那么root即为结果
# O(n) Time
# O(n) Space