# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root: return None

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


'''
# 如果 A 和 B 都在，return  LCA
# 如果只有 A 在，return A
# 如果只有 B 在，return B
# 如果 A, B 都不在，return None
'''
