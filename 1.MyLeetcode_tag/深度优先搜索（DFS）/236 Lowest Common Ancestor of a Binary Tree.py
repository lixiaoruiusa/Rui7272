# 题意：给两个node，找二叉树最接近公共祖先
# 思路：分治
# 如果root == p or root == q 返回root
# 如果左右都找到了返回root (先看左右，再分着看)
# 如果左找到了返回左
# 如果右找到了返回右
# 啥都没有返回None
# Time O(n)
# Space O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right

        return None


