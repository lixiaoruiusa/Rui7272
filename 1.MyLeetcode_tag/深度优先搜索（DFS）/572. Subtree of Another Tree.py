# 题意：检查subRoot是不是root的一部分
# 思路：
"""
判断 t 是否为 s 的子树的三个条件是或的关系，即：
当前两棵树相等；
或者，t 是 s 的左子树；
或者，t 是 s 的右子树。

判断两个树是否相等的三个条件是与的关系，即：
当前两个树的根节点值相等；
并且，s 的左子树和 t 的左子树相等；
并且，s 的右子树和 t 的右子树相等。

"""


# 时间复杂度：时间复杂度为 O(st)
# 空间复杂度: max(O(h1), O(h2))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True

        elif not root or not subRoot:
            return False

        same = self.isSame(root, subRoot)

        left_is_sub = self.isSubtree(root.left, subRoot)
        right_is_sub = self.isSubtree(root.right, subRoot)

        return same or left_is_sub or right_is_sub

    def isSame(self, s, t):
        if not s and not t:
            return True

        elif not s or not t:
            return False

        elif s.val != t.val:
            return False

        left = self.isSame(s.left, t.left)
        right = self.isSame(s.right, t.right)

        return left and right

