# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        result = []

        queue = deque([root])

        while queue:

            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result[::-1]


'''
Time complexity : O(N) since each node is processed exactly once.

Space complexity :O(N) to keep the output structure which contains N node values.

'''