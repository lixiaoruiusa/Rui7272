"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    @Time complexity: O(n)  Space complexity: O(h)

    """
    
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root ==q:
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
        
        
'''
huahua

For a given root, recursively call LCA(root.left, p, q) and LCA(root.right, p, q)

if both returns a valid node which means p, q are in different subtrees, then root will be their LCA.

if only one valid node returns, which means p, q are in the same subtree, return that valid node as their LCA

  def lowestCommonAncestor(self, root, p, q):    
    if any((not root, root == p, root == q)): return root
    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)
    if not l or not r: return l if l else r
    return root
'''

'''
    	# root 等于 p或q
        if root == p or root == q:
            return root
        # p, q 都在左子树
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p, q 都在右子树
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # p, q 分别在左右子树，那么root即为结果
        return root
'''