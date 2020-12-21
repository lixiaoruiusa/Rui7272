"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    @ 可以用recersive吗？
    """
    def inorderTraversal(self, root):
        ans = []
        stack = []
        curr = root
        while curr or stack:
            if not curr:
                curr = stack.pop(-1)
                ans.append(curr.val)
                curr = curr.right
            else:
                stack.append(curr)
                curr = curr.left
        return ans
