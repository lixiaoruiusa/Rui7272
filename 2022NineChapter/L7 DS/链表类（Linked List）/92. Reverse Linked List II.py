# 题意：
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# 思路：
"""
# 第 1 步：从虚拟头节点走 left - 1 步，来到 left 节点的前一个节点
# 建议写在 for 循环里，语义清晰
# 第 2 步：从 pre 再走 right - left + 1 步，来到 right 节点
# 第 3 步：切断出一个子链表（截取链表） # 注意：切断链接
# 第 4 步：同第 206 题，反转链表的子区间
# 第 5 步：接回到原来的链表中
"""


# 时间复杂度：O(N)
# 空间复杂度：O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        prev = dummy
        prev.next = head

        for _ in range(left - 1):
            prev = prev.next

        right_node = prev
        for _ in range(right - left + 1):
            right_node = right_node.next

        # 切断出一个子链表
        left_node = prev.next
        tail = right_node.next

        # 切断链接
        prev.next = None
        right_node.next = None

        self.reverse_linked_list(left_node)

        prev.next = right_node
        left_node.next = tail
        return dummy.next

    def reverse_linked_list(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre