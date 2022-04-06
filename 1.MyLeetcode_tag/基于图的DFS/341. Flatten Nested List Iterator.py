# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
"""
思路： 把nestedList用dfs的方法append到queue中，
       next()时每次popleft
       hasNext()时每次检查queue是否空

时间复杂度：构造函数的时间复杂度是 O(N)
           next()和 hasNext()的时间复杂度是 O(1)
空间复杂度：O(N)

"""


class NestedIterator:
    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = collections.deque()
        self.dfs(nestedList)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
"""
思路： 如果用遍历的方法，就要放一个stack，反向把所有元素append进stack
       next() 直接pop栈顶
       hasNext()时检查是否为数子，不为数字的话，要pop出来，反向重新append进stack


时间复杂度：构造函数的时间复杂度是 O(N)
           next() O(1) 和 hasNext() 的时间复杂度是 O(N)
空间复杂度：O(N)

"""


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            else:
                nest_list = self.stack.pop()
                for nest in reversed(nest_list.getList()):
                    self.stack.append(nest)
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())