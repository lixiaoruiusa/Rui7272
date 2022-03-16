# LFU：least frequently used，最不经常使用；缓存淘汰策略与使用频率和上一次使用时间有关
"""
# key_to_node 是  {key：node}  node含有key，val，freq
# freq 是 {频率：DLinkedList}  DLinkedList里边是node

get
# 如果key不存在则返回-1.
# 如果key存在，则返回对应的value，同时:
  访问频率+1
  将元素从访问频率i的链表中移除，放到频率i+1的链表中

Put操作
# 如果key已经存在，修改对应的value，并将访问频率+1
  将元素从访问频率i的链表中移除，放到频率i+1的链表中
  如果频率i的链表为空，则从频率哈希表中移除这个链表

# 如果key不存在
  缓存超过最大容量，则先删除访问频率最低的元素，再插入新元素
  新元素的访问频率为1，如果频率哈希表中不存在对应的链表需要创建
  缓存没有超过最大容量，则插入新元素
  新元素的访问频率为1，如果频率哈希表中不存在对应的链表需要创建

Min_freq记录全局最小频率，实现O(1) 查找
更新/查找的时候，将元素频率+1，之后如果minFreq不在频率哈希表中了，说明频率哈希表中已经没有元素了，那么minFreq需要+1，否则minFreq不变。
插入的时候，这个简单，因为新元素的频率都是1，所以只需要将minFreq改为1即可


"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.size = 0

    def append(self, node: Node):
        # 尾插入, 加到双向链表尾部, add to tail
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node
        self.size += 1

    def pop(self, node: Node = None):
        if self.size == 0:
            return
        # 删除头部
        if node is None:
            node = self.head.next

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node


# key_to_node 是  {key：node}  node含有key，val，freq
# freq 是 {频率：DLinkedList}  DLinkedList里边是node
import collections
class LFUCache:

    def __init__(self, capacity: int):

        self.key_to_node = {}
        self.freq = defaultdict(DLinkedList)
        self.min_freq = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        node_freq = node.freq
        # 旧的freq移除node，新的freq + 1加入node
        self.freq[node_freq].pop(node)

        # 如果minFreq不在频率哈希表中了，说明频率哈希表中已经没有元素了，那么minFreq需要+1，否则minFreq不变
        if self.min_freq == node_freq and self.freq[node_freq].size == 0:
            self.min_freq += 1
        node.freq += 1
        self.freq[node.freq].append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return  # conner case

        # 如果key存在:
        # 现在key_to_node中拿到node，然后在freq中删除旧的node
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node_freq = node.freq
            self.freq[node_freq].pop(node)
            # 检查这个node是不是最低频率的，如果是的话，要min_freq + 1
            if self.min_freq == node_freq and self.freq[node_freq].size == 0:
                self.min_freq += 1
            # 更新node.freq和node.val 到freq中
            node.freq += 1
            node.val = value
            self.freq[node.freq].append(node)

        else:
            # 如果key不存在
            # capacity满了，就要在两个字典中，删除最低频的这node和node.key
            if len(self.key_to_node) == self.capacity:
                node = self.freq[self.min_freq].pop()
                self.key_to_node.pop(node.key)
            # 建立新的node，分别放入两个字典中，min_freq = 1
            node = Node(key, value)
            self.key_to_node[key] = node
            self.freq[1].append(node)
            self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# lfu = LFUCache(2)
# lfu.put(1, 1)
# lfu.put(2, 2)
# lfu.get(1)