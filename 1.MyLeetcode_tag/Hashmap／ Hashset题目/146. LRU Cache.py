# Time : O(1) for put and get since all operations with ordered dictionary : get/in/set/move_to_end/popitem are done in a constant time.
# Space : O(capacity) for ordered dictionary.
# OrderedDict() 中 popitem vs pop 区别：
# cache.popitem(last=False) pop左边第一元素，默认pop最后
# self.cache.pop(key) pop要有参数key
# 
# from collections import OrderedDict
# class LRUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         # self.cache.move_to_end(key)
#         # return self.cache[key]
#         value = self.cache.pop(key)
#         self.cache[key] = value
#         return value
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.pop(key)
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
# 1 建立double linked list node， 参数为key，value，prev，next
# 2 初始化LRU参数：capacity，cache {key:node}, head,tail 两个node，并且建立两者链接
# 3 get中：取出node，remove_node，add_to_tail, return node.value
# 4 set/put中：如果key存在，remove_node[cache[key]];  建立node，更新cache[key] = node;  add_to_tail; if 超过capacity，pop_front
"""

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key:node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail

    # get O(1) from dict
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return node.value


    # get O(1) from double linkedlist, 
    # it takes constant O(1) time to add and remove nodes from the head or tail

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.add_to_tail(node)
        if len(self.cache) > self.capacity:
            self.pop_front()

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

    def pop_front(self):
        self.cache.pop(self.head.next.key)
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
