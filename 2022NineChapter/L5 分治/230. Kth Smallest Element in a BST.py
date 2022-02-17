# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(H + k) time where H is a tree heigh
# O(N) space in the worst case of the skewed tree
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return stack[-1].val

# Time O(N) to build a traversal.
# Space O(N) to keep an inorder traversal.
# class Solution:
#    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.array = []
#         self.dfs(root)
#         print(self.array)
#         return self.array[k - 1]

#     def dfs(self, root):
#         if not root:
#             return
#         self.dfs(root.left)
#         self.array.append(root.val)
#         self.dfs(root.right)
