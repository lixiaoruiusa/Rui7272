# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(H) time and O(1) space
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return None
        closest_d = float("inf")
        while root:
            if abs(root.val - target) < closest_d:
                closest_d = abs(root.val - target)
                closest = root.val

            if root.val == target:
                return root.val
            elif root.val < target:
                root = root.right
            else:
                root = root.left

        return closest


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
