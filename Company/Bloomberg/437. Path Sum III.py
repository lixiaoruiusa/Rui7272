# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
# Time complexity: O(N), where N is a number of nodes
# Space complexity: O(N)
"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root:
            return 0
        self.count = 0
        self.dfs(root, targetSum)
        return self.count

    def dfs(self, root, targetSum):
        if not root:
            return
        self.dfs(root.left, targetSum)
        self.helper(root, targetSum)
        self.dfs(root.right, targetSum)

    # 每一个node为起点，计算他下边有没有path是targetSum
    # 先3，
    def helper(self, root, targetSum):
        if not root:
            return
        if root.val == targetSum:
            self.count += 1
        self.helper(root.left, targetSum - root.val)
        self.helper(root.right, targetSum - root.val)

"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root: return 0
        count = [0]
        self.dfs(root, targetSum,count)
        return count[0]

    
    def dfs(self, root, targetSum, count):
        if not root: 
            return
        self.dfs(root.left, targetSum, count)
        self.helper(root, targetSum, count)
        self.dfs(root.right, targetSum, count)

        
    def helper(self, root, targetSum, count):
        if not root: 
            return
        if root.val == targetSum: 
            count[0] += 1
        self.helper(root.left, targetSum - root.val, count)
        self.helper(root.right, targetSum - root.val, count)
"""