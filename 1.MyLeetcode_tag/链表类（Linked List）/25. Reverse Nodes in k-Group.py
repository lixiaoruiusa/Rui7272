"""
# 思路：
1 常规操作，找到prev，cur和last_index
2 def reverse，首位都指向None，翻转
3 接回来

Time Complexity: O(N)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            # 检查是否还有k个，last_index向后走k-1步骤
            last_index = cur
            for i in range(k - 1):
                last_index = last_index.next
                if last_index is None:
                    return dummy.next

            # 有k个翻转
            new_head = last_index.next
            r1, r2 = self.reverse(cur, last_index)
            prev.next = r1
            prev = r2
            r2.next = new_head
            cur = new_head

        return dummy.next



    def reverse(self, start, end):

        prev = None
        end.next = None
        cur = start

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return end, start

"""
完全翻版本

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur:
            # 检查是否还有k个，last_index向后走k-1步骤
            last_index = cur
            for i in range(k - 1):
                last_prev = last_index
                last_index = last_index.next
                if last_index is None:
                    r1, r2 = self.reverse(cur, last_prev)
                    prev.next = r1
                    return dummy.next
                
            # 有k个翻转
            new_head = last_index.next
            r1, r2 = self.reverse(cur, last_index)
            prev.next = r1
            prev = r2
            r2.next = new_head
            cur = new_head
        
        return dummy.next
        
    
    
    def reverse(self, start, end):
        
        prev = None
        end.next = None
        cur = start
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return end, start 

"""