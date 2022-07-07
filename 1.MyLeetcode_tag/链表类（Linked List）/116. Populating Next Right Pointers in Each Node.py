"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
思路：利用 previously next指针，有两种情况: 4和5在同一个父节点2上； 5和6不在同一个父节点，但在上层父节点的下一个上
时间复杂度：O(N)，每个节点只访问一次。
空间复杂度：O(1)，不需要存储额外的节点。
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        leftmost = root

        while leftmost.left:
            # 遍历这层
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # 指针向后移动
                head = head.next
            # 去下一层的最左的节点
            leftmost = leftmost.left
        return root


BFS 解法：
Time O(N)
Space： O(N) 因为完全二叉树最后一层为 N/2 所以近似于N
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
    
        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:
            size = len(q) 
            for i in range(len(q)):
                node = q.popleft()
                if i < size - 1:
                    node.next = q[0]
                else:
                    node.next = None
    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
          
        return root

###########################################################
 
        if not root:
            return root

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        for level in res:
            for i in range(len(level)):
                if i == len(level) - 1:
                    level[i].next = None
                else:
                    level[i].next = level[i + 1]
        return root


