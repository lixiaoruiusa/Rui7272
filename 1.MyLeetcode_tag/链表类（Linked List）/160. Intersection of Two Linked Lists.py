# 题意：找到两个linklist相交的点，并返回
# 思路： 两个指针都遍历a+b+c的长度，就指到了公共节点, 如果不相交，正好两个指针指到None
# Time complexity : O(N+M)
# Space complexity : O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB

        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next

            if not p2:
                p2 = headA
            else:
                p2 = p2.next

        return p1 