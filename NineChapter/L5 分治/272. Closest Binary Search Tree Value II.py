# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Nlogk | push N elements into the heap of the size k
# Space complexity:O(k+H)  heap of k elements and the recursion stack of the tree height

import heapq
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        heap = []
        self.inorder_travers(root, target, k, heap)
        res = []
        for distance, val in heap:
            res.append(val)
        return res

    def inorder_travers(self, root, target, k, heap):

        if root is None:
            return
        self.inorder_travers(root.left, target, k, heap)
        heapq.heappush(heap, (-abs(target - root.val), root.val))
        if len(heap) > k:
            heapq.heappop(heap)
        self.inorder_travers(root.right, target, k, heap)


