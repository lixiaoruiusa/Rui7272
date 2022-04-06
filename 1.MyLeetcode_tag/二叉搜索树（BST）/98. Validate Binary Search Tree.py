"""
inorder traverse BST的话，res是从小到大排列，肯定可以，检查结果是否单调增。
Time：O(n)
Space: O(n)
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        res = []
        self.inorder(root, res)
        for i in range(1, len(res)):
            if res[i - 1] >= res[i]:
                return False
        return True

    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

"""
遍历也可以：
所有左边的node入栈，pop
如果node.right也入栈，把new_node = node.right左右的左边也都入栈，保证了stack栈顶一直是最小，根据BST性质
用一个prev记录之前的值,如果prev >= cur就False 
Time：O(n)
Space: O(n)
"""


def isValidBST(self, root: TreeNode) -> bool:
    if not root:
        return

    prev = float("-inf")
    stack = [root]
    while root.left:
        stack.append(root.left)
        root = root.left

    while stack:
        cur = stack.pop()
        if cur.val <= prev:
            return False
        if cur.right:
            stack.append(cur.right)
            new_node = cur.right
            while new_node.left:
                stack.append(new_node.left)
                new_node = new_node.left
        prev = cur.val
    return True