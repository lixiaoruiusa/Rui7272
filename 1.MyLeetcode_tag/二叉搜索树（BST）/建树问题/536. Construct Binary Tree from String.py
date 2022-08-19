# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 类似decode string的方法
# Time Complexity: O(N)
# Space Complexity: O(H) where H represents the height of the tree
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        if not s:
            return None

        stack = []
        is_neg = False
        num = ""

        for i, c in enumerate(s):
            # 如果是负号，单独标记
            if c == "-":
                is_neg = True
            # 把当前的node append到stack，num和is_neg 复原
            elif c == "(":
                stack.append(node)
                num = ""
                is_neg = False
            # 把parent pop出来，要往左或者往右加子树，最后让当前的node = parent
            elif c == ")":
                parent = stack.pop()
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                node = parent
                print(node.val)
            # 每次生成新的node    
            else:
                num += c
                if is_neg:
                    val = -int(num)
                else:
                    val = int(num)

                node = TreeNode(val)

        return node



