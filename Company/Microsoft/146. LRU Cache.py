# Time : O(1) for put and get since all operations with ordered dictionary : get/in/set/move_to_end/popitem are done in a constant time.
# Space : O(capacity) for ordered dictionary.
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
class Node:
    def __init__(self, key= None, value = None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None
        
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}
        self.head = Node(-1,-1) # dummy node
        self.tail = Node(-1, -1) # dummy node
        self.tail.prev = self.head
        self.head.next = self.tail
    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.hash: return -1 
        node = self.hash[key]
        self.remove_node(node)
        self.move_to_tail(node)
        return node.val 
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def put(self, key, value):
        if self.get(key) != -1:
            self.hash[key].val = value
            return 
        if len(self.hash) >= self.capacity:
            self.pop_front()
        node = Node(key, value)
        self.move_to_tail(node)
        self.hash[key] = node
        
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def move_to_tail(self, node):
        node.prev = self.tail.prev 
        node.next = self.tail 
        node.prev.next = node 
        self.tail.prev = node
        
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
'''