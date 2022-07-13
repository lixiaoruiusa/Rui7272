# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
时间复杂度：O(nlogn)，其中 n 是链表的长度。
设长度为 n 的链表构造二叉搜索树的时间为 T(n)，递推式为 T(n) = 2 * T(n/2) + O(n)，根据主定理，T(n) = O(nlogn)。
空间复杂度：O(logn)，这里只计算除了返回答案之外的空间。平衡二叉树的高度为O(logn)，即为递归过程中栈的最大深度，也就是需要的空间。



"""


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if not head:
            return head

        return self.dfs(head)

    def dfs(self, head):
        if not head:
            return None

        if head.next == None:
            return TreeNode(head.val)

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        # Handling the case when slowPtr was equal to head.
        slow.next = None

        root = TreeNode(mid.val)

        root.left = self.dfs(head)
        root.right = self.dfs(mid.next)

        return root