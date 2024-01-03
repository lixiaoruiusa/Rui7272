# 思路：快慢指针找到中点，把二段反转链表，再和第一段比较
# Time complexity : O(n)
# Space complexity : O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow 是中点或者中点右边的点, 全部调到右边的点
        if fast:
            slow = slow.next

        p1 = head
        p2 = self.reverse_linkedlist(slow)

        while p1 and p2:
            if p1.val != p2.val:
                return False
            else:
                p1 = p1.next
                p2 = p2.next
        return True

    def reverse_linkedlist(self, head):

        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev