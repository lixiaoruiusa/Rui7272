# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# 思路：先打擂台记录结果，然后再向下travers
# Time: 二分法binary search，所以是 O(H)
# Space： O(1)
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root: return

        distance = float("inf")
        res = root.val

        while root:

            if distance > abs(root.val - target):
                distance = abs(root.val - target)
                res = root.val

            if root.val == target:
                return root.val
            elif root.val > target:
                root = root.left
            else:
                root = root.right

        return res