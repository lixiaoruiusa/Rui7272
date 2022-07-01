# 题意：把偶数位置的node串联在一起，放在奇数串的后边
# 思路：
# 建立 p1 = odd_head = head 和 p2 = even_head = head.next
# while p2 and p2.next
# 1 -> 3 , 2-> 4 ，最后再把两串链接一起
# Time complexity : O(n)
# Space complexity : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        p1 = odd_head = head
        p2 = even_head = head.next

        while p2 and p2.next:
            p1.next = p2.next
            p1 = p2.next

            p2.next = p1.next
            p2 = p1.next

        p1.next = even_head
        return odd_head

