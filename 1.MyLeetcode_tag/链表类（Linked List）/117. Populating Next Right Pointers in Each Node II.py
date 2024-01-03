"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        cur = root

        while cur:
            # 每下一行的虚拟head，cur是上一行的node
            dummy = Node(0)
            prev = dummy
            while cur:
                if cur.left:
                    prev.next = cur.left
                    prev = prev.next
                if cur.right:
                    prev.next = cur.right
                    prev = prev.next

                cur = cur.next
            cur = dummy.next
        return root

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':

#         if not root:
#             return root

#         q = collections.deque([root])
#         while q:
#             size = len(q)
#             for i in range(size):
#                 cur = q.popleft()
#                 if i < size - 1:
#                     cur.next = q[0]
#                 if cur.left:
#                     q.append(cur.left)
#                 if cur.right:
#                     q.append(cur.right)
#         return root

