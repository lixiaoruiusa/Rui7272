# Solution 1: Ordered dictionary
# O(1) time | O(n) space for ordered dictionary with at most capacity + 1 elements


from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        # do intialization if necessary
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        ## pop value and insert to the bottom of queue
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            ## last = True时pop规则为FILO, last = False时pop规则为FIFO
            self.cache.popitem(last=False)
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 使用了Python自带的OrderedDict, 功能和Java的LinkedHashMap 一样，可以记录存入HashMap的先后顺序。速度也很快，代码也很简短，属于利用高级数据结构取巧的方法