"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# 题意：给一棵二叉树, 找到和为最小的子树, 返回其根节点。
# 思路：分治：维持的三个变量：
# 左子树最小值，左子树根节点，左子树和
# 右子树最小值，右子树根节点，右子树和
# 比较 左子树最小值， 右子树最小值 和 左子树和 + 右子树和 + root.val

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        if not root:
            return None
        subtree_minvalue, subtree, sum_root = self.get_min_subtree(root)
        return subtree


    def get_min_subtree(self, root):
        if root is None:
            return float("inf"), None, 0

        left_minvalue, left_subtree, left_sum_root = self.get_min_subtree(root.left)
        right_minvalue, right_subtree, right_sum_root = self.get_min_subtree(root.right)

        cur_sum_root = left_sum_root + right_sum_root + root.val

        if left_minvalue == min(left_minvalue, right_minvalue, cur_sum_root):
            return left_minvalue, left_subtree, cur_sum_root

        if right_minvalue == min(left_minvalue, right_minvalue, cur_sum_root):
            return right_minvalue, right_subtree, cur_sum_root

        return cur_sum_root, root, cur_sum_root
