# 题意：二叉树 root1 经过不同节点的几次翻转，可以到root2
# 思路：分治
# 递归出口：都空为True，只有一个空Flase，val不相等False
# 递归部分：两种匹配方式
# return match1 or match2

"""
存在三种情况：
1 如果 root1 and root2 都为空，这两个二叉树才等价。
2 如果 root1，root2 的值不相等，那这两个二叉树的一定不等价。
3 当 root1 和 root2 的值相等的情况下，需要继续判断 root1 的孩子节点是不是跟 root2 的孩子节点相当。
 因为可以做翻转操作，所以这里有两种情况需要去判断
"""

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