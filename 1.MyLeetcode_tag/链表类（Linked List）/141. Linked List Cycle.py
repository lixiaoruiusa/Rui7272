# 题意：找有无环，返回True or False
# 思路：快慢指针，如果相遇，就证明有环。
# Time complexity：O(N+K), which is O(n) 无环是n/2，有环是n + k 环里最多k次，就是len of 环，n是未进环的len
# Space complexity : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
