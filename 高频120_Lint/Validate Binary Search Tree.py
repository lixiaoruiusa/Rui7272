"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    @ O(n) time, O(d) space
    """

    def isValidBST(self, root):

        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, tree, min_value, max_value):
        if tree is None:
            return True

        if tree.val <= min_value or tree.val >= max_value:
            return False

        left_is_valid = self.helper(tree.left, min_value, tree.val)
        right_is_valid = self.helper(tree.right, tree.val, max_value)

        return left_is_valid and right_is_valid