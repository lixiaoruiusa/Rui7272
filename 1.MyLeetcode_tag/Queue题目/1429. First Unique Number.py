# 题意：实现showFirstUnique和add number
# 思路：用queue和counter, while queue去找freq == 1的元素，appendleft, return
# Time O(n)
# Space O(n)

import collections


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.queue = collections.deque(nums)
        self.counter = collections.Counter(nums)

    def showFirstUnique(self) -> int:
        while self.queue:
            x = self.queue.popleft()
            if self.counter[x] == 1:
                self.queue.appendleft(x)
                return x
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        self.counter[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)