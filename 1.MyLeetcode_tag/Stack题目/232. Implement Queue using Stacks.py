# 题意： 用两个栈实现一个队列
# 思路：stack1正常栈，stack2用来reverse第一个栈的元素
# push时，append stack1
# pop和peek都要优先检查stack2是否为空，如果空，就transfer stack1的元素进来到stack2
# empty检查两个栈都空


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            value = self.stack1.pop()
            self.stack2.append(value)
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        while self.stack1:
            value = self.stack1.pop()
            self.stack2.append(value)
        return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()