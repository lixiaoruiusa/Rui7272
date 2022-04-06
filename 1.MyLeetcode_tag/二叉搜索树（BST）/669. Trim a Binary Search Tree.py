# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
# 思路：
root.val 共三种情况：
剪裁部分：小于low只保留右子树（因为root和左边都小于low，不在范围内）；
剪裁部分：大于high，只保留左子树（因为root和右边都大于high，不在范围内）；
保留部分：在low和high之间，左树等于剪裁后的左树，右树等于剪裁后的右树。

Time Complexity: O(N)
Space Complexity: O(N)
"""


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        if not root:
            return

        if root.val < low:
            root = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)

        return root

