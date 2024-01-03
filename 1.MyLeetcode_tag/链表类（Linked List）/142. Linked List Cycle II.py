# 题意：找环进循环的node
# 思路：先找有没有环,相遇后再回到起点，一直走一步，相遇点就是进环node
"""
那么相遇时：
slow指针走过的节点数为: a + b
fast指针走过的节点数： a + b + n (b + c)
因为slow和fast有2呗关系，求x：
2 (a + b) = a + b + n (b + c)  =>
a = (n - 1) b + nc = (n - 1) b + nc - c + c
a = (n - 1) (b + c) + c
所以 P1 回到起点， P2在相遇点，再走a个距离，就相遇
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                p1 = head
                p2 = slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None