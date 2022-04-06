# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        balacned, height = self.validate(root)
        return balacned

    def validate(self, root):
        if not root:
            return True, 0

        balacned, left_height = self.validate(root.left)

        if not balacned:
            return False, 0

        balanced, right_height = self.validate(root.right)

        if not balanced:
            return False, 0

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1


'''
？ Time: O(nlogn) | Therefore, the height hh of a balanced tree is bounded by log_{1.5}(n)
                 height will be called on each node O(logn) time.
Space: O(n) | The recursion stack may contain all nodes if the tree is skewed

'''
