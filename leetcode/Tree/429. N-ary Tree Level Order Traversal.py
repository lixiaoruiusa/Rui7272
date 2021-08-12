"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                #queue.extend(node.children)
                for children in node.children:
                    queue.append(children)
            result.append(level)
        return result


'''
Time complexity: O(n) where nn is the number of nodes.
Space complexity: O(n) Same as above, we always have lists containing levels of nodes
'''
