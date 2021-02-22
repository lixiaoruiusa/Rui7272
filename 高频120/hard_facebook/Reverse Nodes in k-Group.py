"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    @ O(n) time | O(1) space
    """
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = left = right = head

        while True:
            count = 0
            while right and count < k:  # use r to locate the range
                right = right.next
                count += 1

            if count == k: # if size k satisfied, reverse the inner linked list
                pre, cur = right, left
                for _ in range(k):
                    cur.next = pre
                    cur = cur.next
                    pre = cur   # standard reversing

                jump.next, jump, left = pre, left, right  # connect two k-groups

            else:
                return dummy.next

