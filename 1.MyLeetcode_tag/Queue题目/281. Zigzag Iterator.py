# deque.popleft() is O(1)
# 题意： 给两个list，锯齿访问
# 思路： 两个queue，因为popleft O(1)

# Time Complexity: O(1) for next and hasNext
# Space Complexity: O(K) k element in queue

import collections


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue1 = collections.deque(v1)
        self.queue2 = collections.deque(v2)
        self.direction = 2

    def next(self) -> int:
        if self.direction == 2 and self.queue1:
            cur = self.queue1.popleft()
            self.direction = 1
        elif self.direction == 1 and self.queue2:
            cur = self.queue2.popleft()
            self.direction = 2
        elif not self.queue1:
            cur = self.queue2.popleft()
            self.direction = 0
        elif not self.queue2:
            cur = self.queue1.popleft()
            self.direction = 0
        return cur

    def hasNext(self) -> bool:
        if not self.queue1 and not self.queue2:
            return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())