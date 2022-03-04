# 题意：返回 middle node of the linked list
# 思路：快慢指针找中点
# Time Complexity: O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         slow = fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next

#         if fast.next != None:
#             return slow.next
#         return slow

# 偶数指出去
# slow = fast = head
# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
# return slow