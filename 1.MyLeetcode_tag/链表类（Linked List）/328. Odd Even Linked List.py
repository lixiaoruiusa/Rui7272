# 题意：把偶数位置的node串联在一起，放在奇数串的后边
# 思路：
# 建立 odd = odd_head = head 和 even = even_head = head.next
# while loop 停止条件为 # 奇数总数时，even为none; 偶数总数时，even.next为none
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

        odd = odd_head = head
        even = even_head = head.next

        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

        odd.next = even_head
        return odd_head

