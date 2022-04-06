# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1


'''
O(N) time |
O(N) space| log(N)最好 the height of the tree log(N)， O(N)最差全在左边，N times recursion
H = 1 + max(H(2-subtree), H(7-subtree))

'''