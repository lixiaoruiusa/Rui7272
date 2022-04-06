# 题意：Binary Tree所有节点左右交换
# 思路：分治，root.left和root.right左右交换
# time complexity is O(n)
# space complexity is O(h) - O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        left_tree = self.invertTree(root.left)
        right_tree = self.invertTree(root.right)
        root.left = right_tree
        root.right = left_tree

        return root
