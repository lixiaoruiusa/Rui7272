# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        # 当左子树或右子树为空时，最小深度取决于另一颗子树
        if left_depth == 0 or right_depth == 0:
            return left_depth + right_depth + 1

        return min(left_depth, right_depth) + 1


'''
# 特别注意：当左子树或右子树为空时，最小深度取决于另一颗子树
时间复杂度O(n)：O(n)，其中 n是节点的数量。我们每个节点只访问一次，因此时间复杂度为 O(n)。
空间复杂度O(n)：考虑到递归使用调用栈（call stack）的情况。
最坏情况：树完全不平衡。例如每个节点都只有左节点，此时将递归n次，需要保持调用栈的存储为O(n)
最好情况：树完全平衡。即树的高度为 log(n)，此时空间复杂度为 O(log(n))
'''