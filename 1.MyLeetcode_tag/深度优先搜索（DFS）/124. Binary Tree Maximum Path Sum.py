# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题意：找二叉树最大path和：可能不过root，可能只包含一部分path
# 思路：二刷
# 1 左右递归，找左右子树的 max_sum ，其实就三种情况，根，根+左，根+右，取最大的
# 2 打擂台，有可能是1 cur_max_sum 2整条连：root.val + left_max_sum + right_max_sum 3 res
# Time O(n)
# Space O(n) 最好O（h）

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [float("-inf")]
        self.dfs(root, max_sum)
        return max_sum[0]

    def dfs(self, root, max_sum):
        if not root:
            return 0

        left_max_sum = self.dfs(root.left, max_sum)
        right_max_sum = self.dfs(root.right, max_sum)

        cur_max_sum = max(left_max_sum + root.val, right_max_sum + root.val, root.val)

        max_sum[0] = max(max_sum[0], cur_max_sum, left_max_sum + right_max_sum + root.val)

        return cur_max_sum


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