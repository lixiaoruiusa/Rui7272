"""
题意：在保留原始顺序的情况下，左边小于x，右边大于等于x
思路：把小于x的放一队，把大于等于的放一队，再拼接.(重点是最后一个要解环)
Time：O(N)  N is the number of nodes in the original linked list
Space：O(1) 只是reforming了原始的list，没有 extra space
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return head

        dummy1 = l1 = ListNode(0)
        dummy2 = l2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next

        # 其实l1和l2的next都可能还指向原来，所以要断一下l2的
        l1.next = None
        l2.next = None
        l1.next = dummy2.next

        return dummy1.next