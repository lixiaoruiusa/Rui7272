# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iteration
# stack 是为了能向上找到，放入右子树的node
# 一定成立，因为preorder，一定是【根 + 小于根的部分 + 大于根的部分】
# Time complexity : O(N) since we visit each node exactly once
# Space complexity : O(N) to keep the stack and the tree


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):

            val = preorder[i]
            node = TreeNode(val)

            # 往左边加容易判断，因为当前val小，就放parent node的左子树
            if val < stack[-1].val:
                stack[-1].left = node
            # 往右边加，要通过stack，向上找到比val小的最后一个node，放入右子树。
            else:
                while stack and stack[-1].val < val:
                    p_node = stack.pop()
                p_node.right = node

            stack.append(node)

        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Recursion
# Time complexity : O(N) since we visit each node exactly once.
# Space complexity : O(N) to keep the entire tree.
# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
#
#         self.index = 0
#         if not preorder: return None
#
#         return self.dfs(float('-inf'), float('inf'), preorder, self.index)
#
#     def dfs(self, lower, upper, preorder, index):
#
#         if self.index == len(preorder):
#             return None
#
#         val = preorder[self.index]
#
#         # 不能造bst
#         if val < lower or val > upper:
#             return None
#
#         self.index += 1
#         node = TreeNode(val)
#         node.left = self.dfs(lower, val, preorder, self.index)
#         node.right = self.dfs(val, upper, preorder, self.index)
#
#         return node




# class Solution:
#     def bstFromPreorder(self, preorder):
#         def dfs(lower, upper):
#
#             nonlocal index
#             if index == len(preorder):  # 遍历到输入最后，退出
#                 return
#             val = preorder[index]  # 获取当前元素
#             if val > upper or val < lower:
#                 return
#             index += 1  # 遍历输入
#             node = TreeNode(val)  # 创建节点
#             node.left = dfs(lower, val)  # 递归创建左右子树
#             node.right = dfs(val, upper)
#             return node
#
#         index = 0
#         return dfs(float("-inf"), float("inf"))