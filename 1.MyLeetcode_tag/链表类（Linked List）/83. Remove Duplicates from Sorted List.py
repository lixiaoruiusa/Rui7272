# Time complexity : O(n)
# Space complexity : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = prev.next
                cur = cur.next

        return dummy.next