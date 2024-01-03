# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time O(N^2)
Space O(N^2)

拆分的前序数组：

左半部分[1,left_count+1)
右半部分[left_count+1,N)
拆分的后序数组：

左半部分[0,left_count)
右半部分[left_count,N-1)


"""


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not postorder:
            return None

        cur = preorder[0]
        root = TreeNode(cur)

        if len(preorder) == 1:
            return root

        # 等号右边的 + 1 表示个数
        left_count = postorder.index(preorder[1]) + 1

        root.left = self.constructFromPrePost(preorder[1: left_count + 1], postorder[: left_count])
        root.right = self.constructFromPrePost(preorder[left_count + 1:], postorder[left_count: - 1])

        return root