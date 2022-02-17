
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.dic = {}

    def insert(self, val: int) -> bool:

        if val in self.dic:
            return False
        self.nums.append(val)
        self.dic[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        deleted = self.dic[val]

        if deleted < len(self.nums) - 1:
            last_num = self.nums[-1]
            self.nums[deleted] = last_num
            self.dic[last_num] = deleted
        del self.dic[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()