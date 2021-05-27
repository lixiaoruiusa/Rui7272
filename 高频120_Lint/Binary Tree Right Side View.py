"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    @ O(n) time, O(depth) space
    """

    def rightSideView(self, root):
        if not root:
            return []
        res = []
        levels = set()
        self.dfs(root, res, levels, 0)
        return res

    def dfs(self, root, res, levels, level):
        if not root:
            return

        if level not in levels:
            res.append(root.val)
            levels.add(level)

        self.dfs(root.right, res, levels, level + 1)
        self.dfs(root.left, res, levels, level + 1)

