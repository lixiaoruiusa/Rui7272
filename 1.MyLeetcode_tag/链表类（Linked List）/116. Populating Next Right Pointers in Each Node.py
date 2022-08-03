"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
题意：一个完美二叉树BT，所有的node都往右边指，最右边的指向Null
思路：利用 previously next指针，
有两种情况: 
4和5在同一个父节点2上； 
5和6不在同一个父节点，但在上层父节点的下一个上

思路2：BFS每次node。next指向q[0]
时间复杂度：O(N)，每个节点只访问一次。
空间复杂度：O(1)，不需要存储额外的节点。
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        cur = root

        while cur:
            # 每下一行的虚拟head，cur是上一行的node
            dummy = Node(0)
            prev = dummy
            # 每次搞的是下一层
            while cur:
                if cur.left:
                    prev.next = cur.left
                    prev = prev.next
                if cur.right:
                    prev.next = cur.right
                    prev = prev.next

                cur = cur.next
            # 当本行都处理完了， 正好换到下一行的头
            cur = dummy.next
        return root


"""
BFS 解法：
Time O(N)
Space： O(N) 因为完全二叉树最后一层为 N/2 所以近似于N

class Solution:
    def connect(self, root: 'Node') -> 'Node':
    
        if not root:
            return root

        q = collections.deque()
        q.append(root)

        while q:
            size = len(q) 
            for i in range(len(q)):
                node = q.popleft()
                # 正好每次指向q[0],是本层下一个node
                if i < size - 1:
                    node.next = q[0]
                else:
                    node.next = None
    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
          
        return root

###########################################################
 
        if not root:
            return root

        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        for level in res:
            for i in range(len(level)):
                if i == len(level) - 1:
                    level[i].next = None
                else:
                    level[i].next = level[i + 1]
        return root


