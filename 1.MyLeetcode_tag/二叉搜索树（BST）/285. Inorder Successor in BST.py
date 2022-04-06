# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 利用二叉搜索树的性质, 比p节点大的在它的右边, 我们只需找到比p节点值大的最小节点.
# 1 如果p的值小于root, 那么我们更新结果为root, 然后往左边搜索.
# 当往右边搜索时, 我们不用更新结果, 因为要么之前已找到更小的结果, 要么还没找到比p节点的值更大的节点.

# 根据BST性质，
# 只有往左去的时候，才会可能是Successor， 往右的话一定不是Successor
# Time Complexity: O(H) ~ O(N)
# Space Complexity: O(1)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        res = None
        while root:
            if p.val < root.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res


# 中序遍历一遍
# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        res = []
        self.inorder(root, res)
        for i in range(1, len(res)):
            if res[i - 1].val == p.val:
                return res[i]
        return None

    def inorder(self, root, res):
        if not root:
            return

        self.inorder(root.left, res)
        res.append(root)
        self.inorder(root.right, res)

