# 题意： sort一个未排序的链表
# 思路： 类似于merge sort
# 用快慢指针倒找mid，把左部分最后置空
# 递归left和right
# 主要递归停止条件return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        slow = head
        fast = head
        # 用快慢指针分成两部分
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 找到左右部分, 把左部分最后置空
        mid = slow.next
        slow.next = None
        # 递归下去
        left = self.sortList(head)
        right = self.sortList(mid)
        # 合并
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode()
        prev = dummy
        l = left
        r = right

        while l and r:
            if l.val < r.val:
                prev.next = l
                l = l.next
                prev = prev.next
            else:
                prev.next = r
                r = r.next
                prev = prev.next
        if l:
            prev.next = l
        if r:
            prev.next = r

        return dummy.next
