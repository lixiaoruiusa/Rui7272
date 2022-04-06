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

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:

        self.res = 0
        self.max_depth = 1
        self.get_depth(nestedList, 1)
        self.dfs(nestedList, self.max_depth)
        return self.res

    def dfs(self, nestedList, depth):

        for nest in nestedList:
            if nest.isInteger():
                self.res += nest.getInteger() * depth
            else:
                self.dfs(nest.getList(), depth - 1)

    def get_depth(self, nestedList, depth):

        self.max_depth = max(self.max_depth, depth)
        for nest in nestedList:
            if nest.isInteger():
                continue
            else:
                self.get_depth(nest.getList(), depth + 1)
