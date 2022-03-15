class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        return self.helper(nestedList, 1)

    def helper(self, nestedList, depth):
        total = 0
        for nested in nestedList:
            if nested.isInteger():
                total += nested.getInteger() * depth
            else:
                total += self.helper(nested.getList(), depth + 1)

        return total