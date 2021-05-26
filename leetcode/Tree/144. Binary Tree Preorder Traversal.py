# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursion
# Time O(n) | Space O(n)

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.dfs(root, res)
#         return res


#     def dfs(self, root, res):
#         if not root:
#             return
#         res.append(root.val)
#         self.dfs(root.left, res)
#         self.dfs(root.right, res)

#         return res

# Solution 2: Stack
# Time O(n) | Space O(n)

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

        return res
