# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
思路：
这个题可以inorder遍历，然后找res中第k个的元素。
更好的解法是：
用stack记录, 一直把左边的node全部入栈，pop出来的时候，如果node.right也入栈；
把新的new = node.right的左右左边也都入栈，这样就保持了stack中，最上边的元素永远是最小的。(BST的性质)

Time complexity: O(logN+k) for the balanced tree, up to O(H + k) 上限O(n)
Space complexity: O(H) to keep the stack, where H is a tree height, up to O(n)
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return

        stack = [root]
        while root.left:
            stack.append(root.left)
            root = root.left

        while k - 1 and stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
                new_node = node.right
                while new_node.left:
                    stack.append(new_node.left)
                    new_node = new_node.left
            k -= 1

        if not stack:
            return
        return stack[-1].val


"""
因为中序遍历BST后，结果就是由小到大排序，return res[k-1] 即可
Time O(n) 遍历了所有nodes
Space O(n) res 占用的空间
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        self.inorder(root, res)
        return res[k - 1]

    def inorder(self, root, res):
        if not root:
            return

        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)