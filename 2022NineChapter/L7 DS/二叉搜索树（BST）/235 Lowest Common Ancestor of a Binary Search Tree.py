# 题意：给p和q，在BST中找公共祖先
# 思路：公共祖先1中，可以spaceO(1)
# 解法： 1 根 > p,q root.left
#       2 根 < p,q root.right
#       3 根与pq一大一小的时候 return root
# Time Complexity: O(N)   n is from h to n
# Space Complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return

        if p.val > q.val:
            p, q = q, p

        while root:
            cur = root.val
            if p.val <= cur <= q.val:
                return root
            elif cur > q.val:
                root = root.left
            else:
                root = root.right

        return None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root