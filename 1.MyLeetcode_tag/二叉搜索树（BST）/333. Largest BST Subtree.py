# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
看到这个题，想到后序遍历，左右根，来判断是否subtree合法。

1 BST合法的条件是：左子树是bst;右子树是bst; root.val > 左子树的最大; root.val < 右子树的最小
返回 True, l_count + r_count + 1, 当前最小, 当前最大

2 如果不合法
返回 False, max(l_count, r_count), 当前最小, 当前最大
# max(l_count, r_count) 有可能下边时合法的，所以统计上最大合法的数值

3 如果 root is None:
返回 True, 0, float('inf'), float('-inf')， 是用来在比较根节点最大最小时，永远成立


时间复杂度O(n)，n是树的节点数量
空间复杂度O(n)
"""


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:

        return self.find_BST(root)[1]

    def find_BST(self, root):

        if root is None:
            return True, 0, float('inf'), float('-inf')
        l_BST, l_count, l_small, l_large = self.find_BST(root.left)
        r_BST, r_count, r_small, r_large = self.find_BST(root.right)

        small = min(root.val, l_small)
        large = max(root.val, r_large)

        if l_BST and r_BST and root.val > l_large and root.val < r_small:
            return True, l_count + r_count + 1, small, large
        return False, max(l_count, r_count), small, large

