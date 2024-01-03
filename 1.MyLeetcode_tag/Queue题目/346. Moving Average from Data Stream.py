# 题意: 生成一个移动窗口的平均数计算器
# 思路：self.count 记录和，append时加上val，pop时减去val
# Time Complexity: O(1)
# Space Complexity: O(n) the size of the queue

import collections
class MovingAverage:

    def __init__(self, size: int):
        self.q = collections.deque()
        self.count = 0
        self.size = size

    #O(1)
    def next(self, val: int) -> float:
        self.q.append(val)
        self.count += val
        if len(self.q) > self.size:
            cur = self.q.popleft()
            self.count -= cur

        return self.count / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)