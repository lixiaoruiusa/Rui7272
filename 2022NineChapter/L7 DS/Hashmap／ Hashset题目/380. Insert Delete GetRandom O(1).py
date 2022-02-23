
"""
# 题意： 类似于实现一个set，有"insert", "remove", "insert", "getRandom"，要求O(1)
# 思路：  val_index_dic = {} 记录val在array中的index
#        insert： 放入array， 存index
#        remove： pop最后一个array的值，与要remove的值在array中交换位置，更新字典
#        getRandom: random.randint(0, len(self.array) - 1)
"""

import random
class RandomizedSet:

    def __init__(self):
        self.val_index_dic = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val not in self.val_index_dic:
            self.array.append(val)
            self.val_index_dic[val] = self.array.index(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.val_index_dic:
            return False

        if self.val_index_dic[val] != len(self.array) - 1:
            new_index = self.val_index_dic[val]
            new_num = self.array.pop()
            self.array[new_index] = new_num
            del self.val_index_dic[val]
            self.val_index_dic[new_num] = new_index
        else:
            self.array.pop()
            del self.val_index_dic[val]
        return True

    def getRandom(self) -> int:
        a = random.randint(0, len(self.array) - 1)
        return self.array[a]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()