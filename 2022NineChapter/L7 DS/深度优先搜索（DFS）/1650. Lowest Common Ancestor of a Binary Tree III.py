# 题意：只给了pq，没有给root，求LCA
# 思路：求depth，然后走到同意depth，再一起向上
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


"""
# 思路：p一直向上，自己和全部parent都入set(); q一直向上，每一步检查是否在set()
# time: O(h)
# space: O(h)
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        s = set()
        while p:
            s.add(p)
            p = p.parent
        while q:
            if q in s:
                return q
            q = q.parent
"""

"""
类似于快慢指针
        point_p = p
        point_q = q
        
        while point_p != point_q:
            
            if point_p.parent:
                point_p = point_p.parent 
            else:
                point_p = q
            
            if point_q.parent:
                point_q = point_q.parent
            else:
                point_q = p
        
        return point_p

"""