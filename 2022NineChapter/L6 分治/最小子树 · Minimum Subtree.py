"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):

        self.min_weight = float("inf")
        self.min_subtree_root = None
        self.get_tree_sum(root)

        return self.min_subtree_root

    def get_tree_sum(self, root):
        if root is None:
            return 0

        left_weight = self.get_tree_sum(root.left)
        right_weight = self.get_tree_sum(root.right)
        root_weight = left_weight + right_weight + root.val

        if root_weight < self.min_weight:
            self.min_weight = root_weight
            self.min_subtree_root = root

        return root_weight



