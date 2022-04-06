# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.left is None and root.right is None and root.val == 0:
            return None

        return root


'''
dfs
Solution: Recursion
Time complexity: O(n) where N is the number of nodes in the tree. We process each node once.
Space complexity: O(h) where H is the height of the tree. This represents the size of the implicit call stack in our recursion.
'''