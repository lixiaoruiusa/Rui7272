# 题意：用queue实现stack
# 思路: 因为只能从左边出，所以每次push都要append(pop) n-1 次，就转化成类似栈一样
# 时间复杂度：入栈操作 O(n)，其余操作都是 O(1)，其中 n 是栈内的元素个数
# 空间复杂度：O(n)，其中 n 是栈内的元素个数
import collections


class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()