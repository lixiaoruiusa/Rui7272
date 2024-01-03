# Time complexity: O(N)
# Space complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur.next = None
                cur = prev.next

            else:
                prev = prev.next
                cur = cur.next

        return dummy.next