# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
"""
思路：dfs求解，每层depth+1， 重点是dfs的时候nest.getList()
Time complexity : O(N)
Space complexity : O(N)
"""


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        self.res = 0
        depth = 1
        self.dfs(nestedList, depth)
        return self.res

    def dfs(self, nestedList, depth):
        if not nestedList:
            return

        for nest in nestedList:
            if nest.isInteger():
                self.res += nest.getInteger() * depth
            else:
                self.dfs(nest.getList(), depth + 1)


