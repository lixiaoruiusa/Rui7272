# 题意：
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# 思路：
"""
# 第 1 步：建立dummy和prev， prev.next = head
# 第 2 步：prev 走到断点之前, 找到prev和left_node
# 第 3 步：prev 被替换再走，找到right_node，和last的位置
# 第 4 步：# 断开, 再反转， 同第 206 题，反转链表的子区间
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

        # 1 -> 2 -> 3 -> 4 -> 5
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


"""
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
        
        for i in range(left - 1):
            prev = prev.next    
        left_node = prev.next
        
        right_node = prev
        
        for i in range(right - left + 1):
            right_node = right_node.next
        
        last = right_node.next
        
        # 1  ->  2  -> 3 ->   4 ->       5
        # prev  left_node    right_node  last
        
        prev.next = None
        right_node.next = None
        
        self.reverse_linkedlist(left_node)
        prev.next = right_node
        left_node.next = last
        
        return dummy.next
    
    
    def reverse_linkedlist(self, head):
        
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.nxt = prev
            prev = cur
            cur = nxt
        return prev
    


"""