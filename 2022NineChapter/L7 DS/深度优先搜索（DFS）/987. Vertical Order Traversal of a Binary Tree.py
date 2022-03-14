# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题意：垂直遍历二叉树，带 i，j坐标，要求坐标相同返回小的.
# [(-2, 2, 4), (-1, 1, 2), (0, 0, 1), (0, 2, 5), (0, 2, 6), (1, 1, 3), (2, 2, 7)]
# 思路：把(j, i, cur.val) 放到list中，排序，最后把相同j坐标的merge

# Time Complexity: O(NlogN)
# Space Complexity: O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return

        node = []
        q = collections.deque()
        q.append((root, 0, 0))

        while q:
            cur, i, j = q.popleft()
            node.append((j, i, cur.val))

            if cur.left:
                q.append((cur.left, i + 1, j - 1))
            if cur.right:
                q.append((cur.right, i + 1, j + 1))

        node = sorted(node)
        #print(node)
        res = []
        cur_col = None
        for col, _, val in node:
            if col != cur_col:
                res.append([val])
                cur_col = col
            elif col == cur_col:
                res[-1].append(val)
        return res

"""
# DFS
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        node = []
        self.dfs(root, 0, 0, node)
        
        node.sort()
        res = []
        cur_col = None
        for col, _, val in node:
            if col != cur_col:
                res.append([val])
                cur_col = col
            elif col == cur_col:
                res[-1].append(val)
        return res

    
    def dfs(self, root, row, col, node):
        
        if not root:
            return
        
        node.append((col, row, root.val))
        self.dfs(root.left, row + 1, col - 1, node)
        self.dfs(root.right, row + 1, col + 1, node)

"""