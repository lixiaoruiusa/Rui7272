"""
题意：删除链表中重复的元素
思路：建立dummy，分两种情况，注意确保while cur and cur.next，因为要比较value

Time complexity: O(N)
Space complexity: O(1)

"""


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
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
                cur = cur.next

            else:
                prev = prev.next
                cur = cur.next

        return dummy.next



