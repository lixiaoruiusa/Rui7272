# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        if not root:
            return []

        paths = []

        self.dfs(root, targetSum, [root.val], paths)

        return paths

    def dfs(self, root, targetSum, path, paths):

        if not root:
            return

        if not root.left and not root.right:
            if sum(path) == targetSum:
                paths.append(list(path))

        if root.left:
            path.append(root.left.val)
            self.dfs(root.left, targetSum, path, paths)
            path.pop()

        if root.right:
            path.append(root.right.val)
            self.dfs(root.right, targetSum, path, paths)
            path.pop()


'''
Time Complexity: O(N^2)
Space Complexity: O(N)

'''



