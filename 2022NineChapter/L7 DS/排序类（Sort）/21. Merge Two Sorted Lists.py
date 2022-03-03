# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        prev = dummy

        left = list1
        right = list2
        while left and right:
            if left.val < right.val:
                prev.next = left
                left = left.next
                prev = prev.next
            else:
                prev.next = right
                right = right.next
                prev = prev.next
        if left:
            prev.next = left
        if right:
            prev.next = right

        print(prev)
        return dummy.next