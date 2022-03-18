# 题意：给p和q，在BST中找公共祖先
# 思路：公共祖先1中，可以spaceO(1)
# 解法： 1 根 > p,q root.left
#       2 根 < p,q root.right
#       3 根与pq一大一小的时候 return root
# Time Complexity: O(N)
# Space Complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


""" 解法2
if root.val == p or root.val == q:
    return root

# p, q 都在左子树
if p.val < root.val and q.val < root.val:
    return self.lowestCommonAncestor(root.left, p , q)

# p, q 都在右子树
if p.val > root.val and q.val > root.val:
    return self.lowestCommonAncestor(root.right, p, q)

# p, q 分别在左右子树，那么root即为结果
return root
"""