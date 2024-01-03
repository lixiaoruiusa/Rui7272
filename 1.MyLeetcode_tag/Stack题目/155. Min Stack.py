# 题目：建立一个MinStack()栈实现一下功能
"""
push(int val)
pop()
top() gets the top element of the stack.
getMin() retrieves the minimum element in the stack.
"""

# 思路：
# 用一个辅助栈当有更<=的值时，入栈。
# 另一个栈正常操作,pop时要检查是否需要pop两个栈

class MinStack:

    def __init__(self):
        self.stack = []
        self.record_min = []

    def push(self, val: int) -> None:
        if val is None:
            return
        self.stack.append(val)
        if not self.record_min or self.record_min[-1] >= val:
            self.record_min.append(val)

    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.record_min[-1]:
            self.record_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.record_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()