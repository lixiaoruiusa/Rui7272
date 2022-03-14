# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 题意：Vertical 遍历 Binary Tree
# 思路：根据输出的性质，top to bottom， left to right，用bfs合适
#      用字典记录{偏移量：[value1, value2, value3]} ，最后sorted(dic.items())一下输出结果
# Time Complexity: O(NlogN)
# Space Complexity: O(N)
import collections


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        dic = {}
        queue = collections.deque()
        queue.append([root, 0])
        while queue:
            cur, key = queue.popleft()
            if key not in dic:
                dic[key] = [cur.val]
            else:
                dic[key].append(cur.val)

            if cur.left:
                queue.append([cur.left, key - 1])
            if cur.right:
                queue.append([cur.right, key + 1])

        res = []
        items = sorted(dic.items())
        for k, v in items:
            res.append(v)
        return res


