# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 题意：奇数层向右遍历，偶数层向左遍历，层级输出结果
# 思路：和level traverse 一样， level的时候用双向队列存结果，向右正常append，向左就appendleft，res.append(list(level))，每层翻转flag
# Time Complexity: O(N)
# Space Complexity: O(N)

import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        flag = True
        queue = collections.deque([root])

        while queue:
            level = collections.deque([])
            for _ in range(len(queue)):
                cur = queue.popleft()
                if flag:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            flag = not flag
            res.append(list(level))

        return res


# 直接level = []版本
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []
        flag = 1
        queue = collections.deque()
        queue.append(root)

        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if flag == 1:
                res.append(level)
                flag = -1
            else:
                res.append(level[::-1])
                flag = 1
        return res
