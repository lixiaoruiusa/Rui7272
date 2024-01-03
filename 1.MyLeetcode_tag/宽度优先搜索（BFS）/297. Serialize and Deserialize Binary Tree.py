# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 题意：二叉树的序列化与反序列化
# 思路：
"""
serialize: bfs遍历，if cur，才有res append（要把int转成str）， if为空，要append "Null"。 用 ",".join(res)返回结果
deserialize: 要检查conner case：  if data[0] == "[]"， 用queue把TreeNode(int(data[i]))放进去，
# 因为null不用操作，相当于skip即可，也不用append到queue中
"""

# BFS
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Codec:

    def serialize(self, root):
        if not root:
            return "[]"

        res = []
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            if cur:
                res.append(str(cur.val))
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append("Null")

        return ",".join(res)

    # <class 'str'>
    # 1,2,3,Null,Null,4,5,Null,Null,Null,Null


    def deserialize(self, data):

        if not data:
            return None
        data = data.split(",")
        i = 0
        if data[i] == "[]":
            return None
        root = TreeNode(data[i])
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            i += 1
            if data[i] != "Null": # 因为null不用操作，不用吧left和right弄上去，相当于skip即可，也不用append到queue中
                cur.left = TreeNode(data[i])
                queue.append(cur.left)
            i += 1
            if data[i] != "Null":
                cur.right = TreeNode(data[i])
                queue.append(cur.right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))