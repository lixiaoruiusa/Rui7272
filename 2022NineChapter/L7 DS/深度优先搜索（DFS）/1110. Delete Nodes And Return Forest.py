# 题意：删除给的node，返回森林
# 思路：
# 1 to_delete去重
# 2 dfs中，返回条件是 if root.val in to_delete，把左右子树append res，返回None； else 返回root
# 3 最后把new_root append到res中
#
# Time: O(n)
# Space : O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        res = []
        to_delete = set(to_delete)
        new_root = self.dfs(root, res, to_delete)

        if new_root is not None:
            res.append(new_root)

        return res

    def dfs(self, root, res, to_delete):
        if not root:
            return

        root.left = self.dfs(root.left, res, to_delete)
        root.right = self.dfs(root.right, res, to_delete)

        if root.val in to_delete:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        else:
            return root