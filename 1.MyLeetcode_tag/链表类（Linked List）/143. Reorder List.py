# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
先找到中点，然后把后半段倒过来，然后前后交替合并
Time:O(N). There are three steps here
Space:O(1)
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        slow = fast = head

        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        if fast:
            p2 = slow.next
            slow.next = None
        else:
            p2 = slow
            prev.next = None

        p1 = head
        p2 = self.reverse(p2)

        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p1 = tmp1
            p2.next = p1
            p2 = tmp2

    def reverse(self, head):

        pre = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre







