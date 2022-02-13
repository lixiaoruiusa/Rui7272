"""
# add O(1)  self.d.get(number, 0) + 1 加入字典
# find O(n) 要判断字典内，n1 == n2 , d.get(num2, 0) >= 2
            或者 n1 ！= n2 , d.get(num2, 0) >= 1
"""

class TwoSum:

    def __init__(self):
        self.d = {}

    def add(self, number: int) -> None:
        if number is not None:
            self.d[number] = self.d.get(number, 0) + 1

    def find(self, value: int) -> bool:
        if value is None:
            return False
        for num1 in self.d:
            num2 = value - num1
            if num2 in self.d and num1 == num2 and self.d.get(num2, 0) >= 2:
                return True
            if num2 in self.d and num1 != num2 and self.d.get(num2, 0) >= 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)