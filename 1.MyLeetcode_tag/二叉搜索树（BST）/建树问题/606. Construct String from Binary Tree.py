# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 分治，没有左右时候返回s，没有右边返回s + l，都有返回 s + l + r
# Time complexity : O(n)  n is depth of tree
# Space complexity : O(n)
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        s = str(root.val)

        l = self.tree2str(root.left)
        r = self.tree2str(root.right)

        if not l and not r:
            return s

        if not r:
            return s + "(" + l + ")"

        return s + "(" + l + ")" + "(" + r + ")"