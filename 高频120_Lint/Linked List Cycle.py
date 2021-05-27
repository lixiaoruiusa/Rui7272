"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    @ 快慢指针的经典题。
      快指针每次走两步，慢指针一次走一步。
      在慢指针进入环之后，快慢指针之间的距离每次缩小1，所以最终能相遇
    @ Time: O(n)  Space O(1)
    """
    def hasCycle(self, head):
        # write your code here
        if head is None or head.next is None:
            return False
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
        