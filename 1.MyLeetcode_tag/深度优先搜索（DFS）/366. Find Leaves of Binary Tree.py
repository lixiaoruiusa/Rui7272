# 题意： 依次从左到右，每次收集并删除所有的叶子节点
"""
          1
         / \
        2   3
       / \
      4   5
输出: [[4,5,3],[2],[1]]
"""


# 思路：

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        self.dfs(root, result)
        return result

    # 返回节点的高度
    def dfs(self, root, result):
        if root is None:
            return -1

        height = -1

        # 高度取决于两个子节点中的较大值
        height = max(height, self.dfs(root.left, result) + 1)
        height = max(height, self.dfs(root.right, result) + 1)

        # 如果高度过大的话，往result中再加一个数组
        if height >= len(result):
            result.append([])

        result[height].append(root.val)

        return height
