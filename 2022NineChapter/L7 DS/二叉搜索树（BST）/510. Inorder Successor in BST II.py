"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
"""
时间复杂度：O(H) ~ O(n) 其中n为数的高度
空间复杂度：O(1)
两种情况：
1 如果有右子树，则右子树最左边的节点就是successor
2 如果没有右子树，说明可能在其上边的某个点（因为左下边的都小啊）
所以向上找节点，直到找到一个node是父节点的左节点，返回这个节点的父节点（正好这个节点大于左子树所有节点，node正好是左子树最大的）
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # 如果有右子树，则右子树最左边的节点就是successor
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # 向上找节点，如果node.parent和 node == node.parent.right 一直是右子树，就往上找
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent

