"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        
        self.helper(root)
        
        return self.maxSum 
        
    def helper(self, root):
        
        if not root:
            return 0 
        
        # 寻找左子树中的最大sub path之和, 出现负数,就清零(i.e., 这条路径不要了)
        leftSum = max(0, self.helper(root.left))
        # 寻找右子树中的最大sub path之和, 出现负数,就清零(i.e., 这条路径不要了)
        rightSum = max(0, self.helper(root.right))
        
        '''
        # self.maxSum是一个全局变量,用来追踪全局最大值
        # left + right + node.val这个式子其实涵盖了case1-3, 因为在上一步,如果左子树sub path之后或右子树sub path之和为负数的话,会被清零
        # 因为left和right有0的情况,所以这个式子可以看成:
        #       left + node.val
        #       right + node.val
        #       left + right + node.val
        '''
        self.maxSum = max(self.maxSum, root.val + leftSum + rightSum)
        
        # 返回的值是可供上一层父节点接龙的值
        return max(root.val + leftSum, root.val + rightSum)