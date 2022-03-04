# 题意：反转链表
# 思路：
# 三个指针的初始化：pre指向空节点，cur指向头结点head，nxt指向head.next
# 因为head.next可能不存在，nxt在循环中定义，这样如果head为空就不会进入循环
# 迭代过程
"""
nxt指向cur.next
cur.next指向pre
pre移动到cur位置
cur移动到nxt位置

"""

# 时间复杂度：O(n)
# 空间复杂度：O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre