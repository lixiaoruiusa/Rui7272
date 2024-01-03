# 题意:一个敲钟计数器 能统计300秒以内敲击的数量
# 思路：用queue来实现， gethit时大于区间的值出队， timestamp - x < 300的值，appendleft，return len（queue）
# hit：  O(1) time,
# getHits： O(N) time
# space O(N)
import collections
class HitCounter:

    def __init__(self):
        self.q = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()
        if not self.q:
            return 0
        return len(self.q)


# class HitCounter:
#
#     def __init__(self):
#         self.queue = collections.deque()
# 
#     def hit(self, timestamp: int) -> None:
#         self.queue.append(timestamp)
#
#     def getHits(self, timestamp: int) -> int:
#         while self.queue:
#             x = self.queue.popleft()
#             if timestamp - x < 300:
#                 self.queue.appendleft(x)
#                 return len(self.queue)
#        return 0

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)