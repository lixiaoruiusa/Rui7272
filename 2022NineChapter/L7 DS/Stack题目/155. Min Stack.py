# 题目：建立一个MinStack()栈实现一下功能
"""
#push(int val) pushes the element val onto the stack.
#pop() removes the element on the top of the stack.
#top() gets the top element of the stack.
#getMin() retrieves the minimum element in the stack.
"""


# 思路：
# 用一个辅助栈当mintopstack，如果<= min_top_stack[-1]时要入栈。另一个栈正常操作,pop时要检查是否需要pop两个栈
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_top_stack = []

    def push(self, val: int) -> None:
        if not self.stack and not self.min_top_stack:
            self.stack.append(val)
            self.min_top_stack.append(val)
        else:
            self.stack.append(val)
            if val <= self.min_top_stack[-1]:
                self.min_top_stack.append(val)

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.min_top_stack[-1]:
            self.min_top_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_top_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()