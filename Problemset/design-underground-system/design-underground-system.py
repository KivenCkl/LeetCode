
# @Title: 设计地铁系统 (Design Underground System)
# @Author: KivenC
# @Date: 2020-07-21 17:54:49
# @Runtime: 240 ms
# @Memory: 22.6 MB

class UndergroundSystem:

    def __init__(self):
        self.tmp = dict()
        self.data = collections.defaultdict(lambda : [0, 0])


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.tmp[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_info = self.tmp.pop(id)
        key = (in_info[0], stationName)
        self.data[key][0] += t - in_info[1]
        self.data[key][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        data = self.data[(startStation, endStation)]
        return data[0] / data[1]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
