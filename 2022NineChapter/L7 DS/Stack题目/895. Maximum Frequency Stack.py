"""
题意：类似stack的结构，pop 频率最高的值，如果频率相等，pop后入栈的值
思路：
1 两个dict，一个记录频率counter，
  一个记录最大频率group = {3:[5,7], 2:[5,7,2],1:[5,7,2,6]}
  maxfreq = 0 记录实时 maxfreq
2 push和pop的时候同时更新counter，group 和 maxfreq

"""

# Time Complexity: O(1)O(1) for both push and pop operations.
# Space Complexity: O(N)

class FreqStack:

    def __init__(self):
        self.counter = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.counter[val] = self.counter.get(val, 0) + 1
        if self.counter[val] > self.maxfreq:
            self.maxfreq = self.counter[val]
        self.group[self.counter[val]].append(val)

    def pop(self) -> int:
        num = self.group[self.maxfreq].pop()
        self.counter[num] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()