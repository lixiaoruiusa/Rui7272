# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题意：找BST中最接近target的点，返回root.val
# 思路：打擂台，往target的方向走
# O(H) time and O(1) space
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return

        closest = float("inf")
        res = root.val

        while root:
            if abs(root.val - target) < closest:
                closest = abs(root.val - target)
                res = root.val

            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                return root.val
        return res

"""

class Solution:
    def closestValue(self, root, target):
        if root is None:
            return None

        return self.helper(root, target, root.val)

    def helper(self, root, target, closest):
        if root is None:
            return closest

        if abs(root.val - target) < abs(closest - target):
            closest = root.val

        if root.val < target:
            return self.helper(root.right, target, closest)
        else:
            return self.helper(root.left, target, closest)
"""