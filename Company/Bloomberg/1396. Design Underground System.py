from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.user = {}
        self.station = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.user[id]
        self.station[(startStation, stationName)].append(t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tmp = self.station[(startStation, endStation)]
        return sum(tmp) / len(tmp)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# user = {id: (stationName, t)}
# station = {(startStation, stationName): 15-3 = 12, 22-8 = 14}
# checkIn O(1)
# checkOut O(1)
# getAverageTime O(n)


undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(45, "Leyton", 3)
undergroundSystem.checkIn(32, "Paradise", 8)
undergroundSystem.checkIn(27, "Leyton", 10)
undergroundSystem.checkOut(45, "Waterloo", 15)
print(undergroundSystem.getAverageTime("Leyton","Waterloo"))

