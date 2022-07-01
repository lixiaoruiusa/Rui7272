"""
题意： 1 -> 2 -> 3 -> 4 两两翻转成  2 -> 1 -> 4 -> 3
思路： 基本操作，先找到second和third，断开重连.
Time Complexity : O(N) where N is the size of the linked list.
Space Complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            second = cur.next
            third = cur.next.next
            # 断
            prev.next = second
            second.next = cur
            cur.next = third

            prev = cur
            cur = cur.next

        return dummy.next









