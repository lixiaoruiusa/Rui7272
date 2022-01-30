"""
# add O(1)
# find O(n)
# 特别注意： and (value - num != num or self.count[num] > 1
"""
class TwoSum:

    def __init__(self):
        self.count = {}

    def add(self, number: int) -> None:
        # add O(1)
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1

    def find(self, value: int) -> bool:
        # find O(n)
        for num in self.count:
            if value - num in self.count and (value - num != num or self.count[num] > 1):
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)