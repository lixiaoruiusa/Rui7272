# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        r = root
        s = subRoot
        
        if not r and not s:
            return True
        if not r or not s:
            return False
        
        if self.isSametree(r, s):
            return True
        
        return self.isSubtree(r.left, s) or self.isSubtree(r.right, s)
        
     
    def isSametree(self, r, s):
        if not r and not s:
            return True
        if not r or not s:
            return False
        
        if r.val != s.val:
            return False
        
        return self.isSametree(r.left, s.left) and self.isSametree(r.right, s.right)
        

'''
时间复杂度：O(ST) 对于每一个s上的点，都需要做一次深度优先搜索来和t匹配，匹配一次的时间代价是 O(|t|)，那么总的时间代价就是 O(|s|*|t|)
空间复杂度：max(ds,dt) 假设s深度为 ds, t的深度为 dt
'''