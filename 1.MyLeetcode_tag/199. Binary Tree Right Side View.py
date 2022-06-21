# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time complexity: O(N) since one has to visit each node.
# Space complexity: O(D) to keep the queues, where D is a tree diameter.
# level travers的时候，只把最右边append到结果
# 需要注意的需要提前记忆level_length，因为for循环下边会变
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        right_side = []
        queue = collections.deque([root])
        while queue:
            # 需要提前记忆level_length，因为for循环下边会变
            level_length = len(queue)

            for i in range(len(queue)):

                cur = queue.popleft()
                if i == level_length - 1:
                    right_side.append(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return right_side

# level travers的方法

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        if not root:
            return []

        res = []
        queue = collections.deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(level)

        output = []
        for r in res:
            output.append(r[-1])
        return output
