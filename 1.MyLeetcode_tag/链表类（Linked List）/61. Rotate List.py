"""
思路： 求length，处理k，求n = length - (k % length)， 最后链接tail到head
Time: O(N)
Space: O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        p1 = head
        length = 0
        while p1:
            length += 1
            p1 = p1.next
            tail = tail.next

        if k % length == 0:
            return head

        n = length - (k % length)

        prev = dummy
        cur = head
        for i in range(n):
            prev = prev.next
            cur = cur.next

        prev.next = None
        tail.next = head

        return cur