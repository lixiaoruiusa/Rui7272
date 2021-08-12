# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        res = []

        if not root:
            return True

        return self.dfs(root, res)

    def dfs(self, node, res):

        if node:
            res.append(node.val)
            self.dfs(node.left, res)
            self.dfs(node.right, res)

        return len(set(res)) == 1


'''
dfs tree， 把value放到set里
O(n) Time |
O(n) Space |
'''

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
            if not root:
                return True
           
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
'''