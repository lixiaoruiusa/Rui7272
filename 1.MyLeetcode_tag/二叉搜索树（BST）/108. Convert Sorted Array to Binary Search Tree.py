# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
思路：
因为已经排好顺序了，所以中间点就是root
root.left 就是往左切分返回的tree
root.right 就是往右切分返回的tree
停止条件是l > r
Time complexity: O(N) since we visit each node exactly once.
Space complexity: O(logN).
The recursion stack requires O(logN) space because the tree is height-balanced
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        if not nums:
            return None
        l = 0
        r = len(nums) - 1
        root = self.build_tree(nums, l, r)
        return root

    def build_tree(self, nums, l, r):
        # 当l=r时候还有最后一个值，例如l=r=0
        if l > r:
            return

        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.build_tree(nums, l, mid - 1)
        root.right = self.build_tree(nums, mid + 1, r)

        return root