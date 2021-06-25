# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        q = [root]
        while q:
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            if not tmp:
                return sum([n.val for n in q])
            q = tmp

        return 0


'''
# 按层进行BFS，如果下一层没有新的节点，返回当前层所有数的和
Time O(N) since one has to visit each node.
Space O(N) to keep the queue.
'''