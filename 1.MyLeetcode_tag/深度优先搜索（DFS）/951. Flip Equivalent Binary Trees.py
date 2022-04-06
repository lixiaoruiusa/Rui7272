# 题意：二叉树 root1 经过不同节点的几次翻转，可以到root2
# 思路：分治
# 递归出口：都空为True，只有一个空Flase，val不相等False
# 递归部分：两种匹配方式
# return match1 or match2

# Time Complexity: O(N)
# Space Complexity: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False

        match1 = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        match2 = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

        if match1 or match2:
            return True
        return False