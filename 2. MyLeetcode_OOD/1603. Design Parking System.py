# 使用一个数组储存停车位剩余的数量

class ParkingSystem:

    def __init__(self, big, medium, small):
        self.lots = [0, big, medium, small]

    def addCar(self, carType):
        if self.lots[carType] == 0:
            return False
        self.lots[carType] -= 1
        return True

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)