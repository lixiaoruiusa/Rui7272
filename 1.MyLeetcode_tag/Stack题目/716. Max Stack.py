"""
类似于Min stack的方法，区别是popMax时候要加入一个buff的临时stack，找到最大值后，再放回主stack
"""


class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_record = []

    def push(self, x: int) -> None:
        if x is not None:
            self.stack.append(x)
            if not self.max_record or x >= self.max_record[-1]:
                self.max_record.append(x)

    def pop(self) -> int:
        if not self.stack:
            return
        cur = self.stack.pop()
        if cur == self.max_record[-1]:
            self.max_record.pop()
        return cur

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1]

    def peekMax(self) -> int:
        if not self.max_record:
            return
        return self.max_record[-1]

    # O(N) for the popMax operation
    def popMax(self) -> int:
        if not self.max_record:
            return
        buffer = []
        cur_max = self.max_record.pop()
        while self.stack and self.stack[-1] != cur_max:
            buffer.append(self.stack.pop())
        res = self.stack.pop()
        while buffer:
            self.push(buffer.pop())
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()