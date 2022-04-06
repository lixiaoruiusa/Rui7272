# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        return self.dfs(root, "")

    def dfs(self, root, current_sum):
        if not root:
            return 0

        current_sum += str(root.val)

        if not root.left and not root.right:
            return int(current_sum)

        return self.dfs(root.left, current_sum) + self.dfs(root.right, current_sum)

# O(N) time |
# O(H) space | keep the recursion stack, height
