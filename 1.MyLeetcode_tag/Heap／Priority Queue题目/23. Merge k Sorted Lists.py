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
# Time：O(nlogk)  number of total N nodes, k lists
# Space: O(n)
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        h = []
        count = 0
        for linked_list in lists:
            if linked_list:
                heapq.heappush(h, [linked_list.val, count, linked_list])
                count += 1

        # keep popping out of the heap
        dummy = ListNode(0)
        cur = dummy
        while h:
            _, _, node = heapq.heappop(h)
            # add node and move current node
            cur.next = node
            cur = cur.next
            node = node.next
            # whichever node was the smallest, its next will be added to the heap, if it is not null
            if node:
                heapq.heappush(h, [node.val, count, node])
                count += 1
        # get the dummy node's next. Which is the head
        return dummy.next


# 两两merge的方法
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        left = self.merge_range_lists(lists, start, mid)
        right = self.merge_range_lists(lists, mid + 1, end)
        return self.merge_two_lists(left, right)


    def merge_two_lists(self, head1, head2):
        tail = dummy = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        if head2:
            tail.next = head2

        return dummy.next

