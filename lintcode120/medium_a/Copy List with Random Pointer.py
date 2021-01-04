"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
    
    @ please see the problme 137 clone graph.
      use the hash map/ dict to mapping the node: new node
      Space: O(n)
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
            
        #  mapping the node to new node
        dic = {}
        curr = head
        while curr:
            dic[curr] = RandomListNode(curr.label)
            curr = curr.next

        #  copy the next and ramdon pointer
        for node in dic:
            if node.next:
                dic[node].next = dic[node.next]
            if node.random:
                dic[node].random = dic[node.random]
                
        return dic[head]