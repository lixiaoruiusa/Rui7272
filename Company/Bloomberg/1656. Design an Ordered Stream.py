"""
题意： 返回self.ptr这个指针的和大于等于他的值，
{3: "cccc"}
"""


class OrderedStream:

    def __init__(self, n: int):
        self.dic = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.dic[idKey] = value

        res = []
        while self.ptr in self.dic:
            res.append(self.dic[self.ptr])
            self.ptr += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)