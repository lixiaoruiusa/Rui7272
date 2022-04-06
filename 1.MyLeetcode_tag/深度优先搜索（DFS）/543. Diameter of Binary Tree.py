# 题意：求二叉树的最大直径
# 思路：dfs分治的方法求left_height right_height和root_height， 唯一注意的是有可能left + right 是最长
# Time complexity: O(N)  N is the number of nodes
# Space complexity: O(H) ~ O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        self.dfs(root)
        return self.longest

    def dfs(self, root):
        if root is None:
            return 0

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        root_height = 1 + max(left_height, right_height)

        self.longest = max(self.longest, left_height + right_height)

        return root_height
