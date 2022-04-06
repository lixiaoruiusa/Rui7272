# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1: Recursion
# Time O(n) | Space O(n)
# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.helper(root, res)
#         return res
#
#     def helper(self, root, res):
#         if not root:
#             return
#
#         self.helper(root.left, res)
#         self.helper(root.right, res)
#         res.append(root.val)
#
#         return res

# Solution 2: stack
# The 2nd uses modified preorder (right subtree first). Then reverse the result.
# Time O(n) | Space O(n)
# 后续遍历是先左子树，再右子树再到父结点，倒过来看就是先父结点，再右子树再左子树。 是前序遍历改变左右子树访问顺序。 再将输出的结果倒序输出一遍就是后序遍历。

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        stack = [root]
        res = []

        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)

        return res[::-1]