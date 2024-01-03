# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Time O(N)
# Space O(N)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        cur = max(left_height, right_height) + 1

        return cur

# 二刷：
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         res = [0]
#         self.dfs(root, res)
#         return res[0]
#
#     def dfs(self, root, res):
#         if not root:
#             return 0
#
#         left_height = self.dfs(root.left, res)
#         right_height = self.dfs(root.right, res)
#
#         cur = max(left_height, right_height) + 1
#         res[0] = max(res[0], cur)
#
#         return cur


"""
# Time O(N)
# Space O(N)

        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth

"""
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        cur = max(left_height, right_height) + 1

        return cur
"""