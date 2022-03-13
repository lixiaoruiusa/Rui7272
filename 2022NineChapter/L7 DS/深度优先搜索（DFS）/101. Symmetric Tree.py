# 题意：看是否为mirror tree
# 思路：isMirror(root, root) 检查，
# 分治
# 都空为T，
# 只有一个空F，
# 左边 = isMirror(root1.left, root2.right) 右边= isMirror(root1.right, root2.left)
# 返回 左边 and 右边
# Time complexity : O(n)
# Space complexity : O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.isMirror(root, root)

    def isMirror(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 and root2:
            return False
        if root1 and not root2:
            return False

        if root1.val != root2.val:
            return False

        L = self.isMirror(root1.left, root2.right)
        R = self.isMirror(root1.right, root2.left)

        return L and R


