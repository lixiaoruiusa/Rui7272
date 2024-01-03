# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 题意：merge 多个sorted linked list
# 思路：1 把每个list的第一个node放入heap，as [linked_list.val, counter, linked_list]
#      2 count的作用是heap不能比较node，防报错
#      3 cur_node = dummy， 然后pop， add node and move current
#      4 if node.next存在，把[node.next.val, counter, node.next)] 加入heap
# Time：O(nlogk)
# Space: O(n)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        heap = []
        dummy = ListNode()

        counter = 0
        for linked_list in lists:
            if linked_list:
                heapq.heappush(heap, [linked_list.val, counter, linked_list])
                counter += 1

        # keep popping out of the heap
        cur_node = dummy
        while heap:
            _, _, node = heapq.heappop(heap)
            # add node and move current node
            cur_node.next = node
            cur_node = cur_node.next

            # whichever node was the smallest, its next will be added to the heap, if it is not null
            if node.next:
                heapq.heappush(heap, [node.next.val, counter, node.next])
                counter += 1

        # get the dummy node's next. Which is the head
        return dummy.next