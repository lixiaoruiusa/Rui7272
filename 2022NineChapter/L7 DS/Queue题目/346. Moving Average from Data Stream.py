# 题意: 生成一个移动窗口的平均数计算器
# 思路：不能每次都sum/n，所以用一个window_sum来记录running和，类似于移动双指针
# Time Complexity: O(1)
# Space Complexity: O(N) the size of the moving window

import collections


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.window_sum += val
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()

        return self.window_sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)