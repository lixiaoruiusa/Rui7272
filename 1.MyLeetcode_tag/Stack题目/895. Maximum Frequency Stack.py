"""
题意：类似stack的结构，pop 频率最高的值，如果频率相等，pop后入栈的值
思路：
1 两个dict，一个记录频率counter，
  一个记录最大频率group = {3:[5,7], 2:[5,7,2],1:[5,7,2,6]}
  maxfreq = 0 记录实时 maxfreq
2 push和pop的时候同时更新counter，group 和 maxfreq

"""

# Time Complexity: O(1) for both push and pop operations.
# Space Complexity: O(N)

class FreqStack:

    def __init__(self):
        self.counter = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        # push的时候 1更新counter 2如果更大了，更新maxfreq 3把值append到频率组里
        self.counter[val] = self.counter.get(val, 0) + 1
        if self.counter[val] > self.maxfreq:
            self.maxfreq = self.counter[val]

        self.group[self.counter[val]].append(val)

    def pop(self) -> int:
        # as 5 and 7 is the most frequent, but 7 is closest to the top
        # 所以正好从group[self.maxfreq]里pop
        num = self.group[self.maxfreq].pop()
        # 更新counter
        self.counter[num] -= 1
        # 如果self.maxfreq的组空了，就self.maxfreq -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()