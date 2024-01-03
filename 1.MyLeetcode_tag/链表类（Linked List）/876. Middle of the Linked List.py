# 题意：返回 middle node of the linked list
# 思路：快慢指针找中点
# 同一层，分别走一步两步，while fast和fast.next ，slow落在中点或者中点右边
# Time Complexity: O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:


        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow