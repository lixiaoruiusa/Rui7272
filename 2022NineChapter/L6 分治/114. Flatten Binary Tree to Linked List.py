# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time and O(n) space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return None

        left_last = self.helper(root.left)
        right_last = self.helper(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root