# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(H + k) time where H is a tree height This complexity is defined by the stack, which contains at least H+k elements
# Space complexity: O(H) to keep the stack, where H is a tree height
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack = []
        # 一路向左，把树左边的node全部入栈
        while root:
            stack.append(root)
            root = root.leftt

        for i in range(k - 1):
            # 前一个元素出栈
            node = stack.pop()
            # 如果右子树不空，进入右子树
            if node.right:
                node = node.right
                # 一路向左，把左边的node全部入栈（因为左边包含了左边和中间）
                while node:
                    stack.append(node)
                    node = node.left

        # 当前栈顶就是第k个元素
        return stack[-1].val

"""
# O(H + k) time where H is a tree heigh
# O(N) space in the worst case of the skewed tree

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root, k, res)
        return res[k - 1]

    def inorder(self, root, k, res):
        if root is None:
            return None

        self.inorder(root.left, k, res)
        res.append(root.val)
        self.inorder(root.right, k, res)
"""
