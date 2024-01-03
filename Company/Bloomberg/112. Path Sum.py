# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        return self.dfs(root, targetSum, 0)

    def dfs(self, root, targetSum, currentSum):
        if not root:
            return None

        currentSum += root.val
        if not root.left and not root.right:
            return currentSum == targetSum

        left = self.dfs(root.left, targetSum, currentSum)
        right = self.dfs(root.right, targetSum, currentSum)

        if left or right:
            return True
        return False