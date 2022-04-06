# 题意： 给了preorder和inorder的顺序，构造Binary Tree
# 思路：preorder: 根左右   inorder：左根右  
# root = TreeNode(preorder[0])
"""
pre = [3,9,20,15,7]  in = [9,3,15,20,7]
------------------------------------------------------
left:  preorder[1:mid+1] inorder[:mid]    左子树有mid数量的元素
right: preorder[mid+1:], inorder[mid+1:]  右子树有[mid+1：]的元素数量
------------------------------------------------------
                root(3)
left:pre [9,20,15,7]  right: ?
left:in [9]           right: in [15,20,7]
------------------------------------------------------
                root(3)
        root(9)     right: pre [20,15,7]
                    right: in [15,20,7]
------------------------------------------------------
                root(3)
        root(9)          root(20)
               left: pre [15,7]  right: pre ?
               left: in [15]     right: in [7]
------------------------------------------------------
                root(3)
        root(9)          root(20)
                   root(15)  right: pre [7]
                             right: in [7]


"""


# Time complexity : O(N)
# Space complexity : O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root