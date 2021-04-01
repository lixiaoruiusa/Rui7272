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

            if count == k:  # if size k satisfied, reverse the inner linked list
                pre = right
                cur = left
                for _ in range(k):
                    cur.next = pre
                    cur = cur.next
                    pre = cur  # standard reversing

                jump.next = pre
                jump = left
                left = right  # connect two k-groups

            else:
                return dummy.next


'''
def reverseList(self, head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev
'''