# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Recursion
# Time O(n) | Space O(n)
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.helper(root, res)
#         return res
#
#     def helper(self, root, res):
#         if not root:
#             return
#
#         self.helper(root.left, res)
#         res.append(root.val)
#         self.helper(root.right, res)
#
#         return res

# Solution 2: Stack
# Time O(n) | Space O(n)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = []
        res = []
        curr = root
        # 左边全部压入stack里， pop后，检查curr.right, 压入stack里
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res