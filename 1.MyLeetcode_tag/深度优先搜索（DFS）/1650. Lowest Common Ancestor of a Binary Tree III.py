# 题意：只给了pq，没有给root，求LCA， p and q exist in the tree
# 思路：求depth，然后走到同一depth，再一起向上
# time: O(n)
# space: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_depth = self.get_depth(p)
        q_depth = self.get_depth(q)

        # 放到了同一层
        for _ in range(p_depth - q_depth):
            p = p.parent
        for _ in range(q_depth - p_depth):
            q = q.parent

        # 一起同时向上
        while p != q:
            p = p.parent
            q = q.parent
        return p

    def get_depth(self, p):

        depth = 0
        while p:
            p = p.parent
            depth += 1
        return depth


# 思路：p全部parent都入set(); q一直向上check set()
# time: O(h)
# space: O(h)
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while p:
            visited.add(p.val)
            p = p.parent

        while q:
            if q.val in visited:
                return q
            q = q.parent
        return -1


"""
和链表相交一样，双指针
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p_hat = p
        q_hat = q
        
        while p_hat != q_hat:
            
            if p_hat.parent:
                p_hat = p_hat.parent 
            else:
                p_hat = q
            
            if q_hat.parent:
                q_hat = q_hat.parent
            else:
                q_hat = p
        
        return p_hat
"""