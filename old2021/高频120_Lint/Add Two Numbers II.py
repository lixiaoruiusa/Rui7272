"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        stack1 = []
        stack2 = []
        dummy = ListNode(-1)
        
        # list node value to stack
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        # add stack value 
        carry = 0
        while stack1 or stack2 or carry:
            tmp1 = tmp2 = 0
            if stack1:
                tmp1 = stack1.pop()
            if stack2:
                tmp2 = stack2.pop()
            
            mod = (tmp1 + tmp2 + carry) % 10
            carry = (tmp1 + tmp2 + carry) // 10
            
            # 头插法插入节点
            new_node = ListNode(mod)
            new_node.next = dummy.next
            dummy.next = new_node
        return dummy.next
        