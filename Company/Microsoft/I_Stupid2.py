# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
from collections import OrderedDict


class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = OrderedDict()


    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            self.cache[key] = value
        self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.maxSize:
            self.cache.popitem(last=False)


    def getValueFromKey(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value


    def getMostRecentKey(self):
        if not self.cache:
            return -1
        key, value = self.cache.popitem()
        self.cache[key] = value
        return value


obj1 = LRUCache(3)
obj1.insertKeyValuePair("b", 2)
