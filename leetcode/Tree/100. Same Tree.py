# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


'''
# Recursion
O(n) Time |
O(n) Space | O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.

1 Both are empty: same
2 One is empty: not the Same
3 Both are not empty, compare the root value
4 Compare left-subtree and right-subtree recursively.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        stack = [(p, q)]
        while stack:
            p, q = stack.pop()

            if not self.check(p, q):
                return False

            if p:
                stack.append((p.right, q.right))
                stack.append((p.left, q.left))
        return True

    def check(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return True


'''
O(n) Time |
O(n) Space | Keep stack nlogn best case O(n) worst case of completely unbalanced tree
'''

