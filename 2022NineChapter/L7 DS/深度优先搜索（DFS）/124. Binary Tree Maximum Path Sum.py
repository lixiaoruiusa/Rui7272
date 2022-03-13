# 题意：找二叉树最大path和：可能不过root，可能只包含一部分path
# 思路：真的不难。
# 1 左右递归，root_max_sum 就三种情况，根自己，根左，根右，取最大的
# 2 全局变量打擂台，有可能是不过根的路径和最大，所以取res，root_max_sum，root.val + left_max_sum + right_max_sum的最大
# Time O(n)
# Space O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left_max_sum = self.dfs(root.left)
        right_max_sum = self.dfs(root.right)

        root_max_sum = max(root.val, root.val + left_max_sum, root.val + right_max_sum)

        self.res = max(self.res, root_max_sum, root.val + left_max_sum + right_max_sum)

        return root_max_sum