import math
from collections import defaultdict

def calMin(time):
    timeArr = time.split(':')
    result = int(timeArr[0])*60 + int(timeArr[1])
    return result;

class Cars:
    def __init__(self, fees):
        self.fees = fees
        self.flag = False
        self.inTime = 0
        self.totalTime = 0
    
    def update(self, inout, time):
        self.flag = True if inout == 'IN' else False
        if self.flag:
            self.inTime = calMin(time)
        else:
            self.totalTime += calMin(time) - self.inTime
    
    def getMoney(self):
        if self.flag == True:
            self.update('OUT', '23:59')
        money = self.fees[1]
        if self.totalTime > self.fees[0]:
            money += math.ceil((self.totalTime - self.fees[0])/self.fees[2])*self.fees[3]
        return money

def solution(fees, records):
    carsDict = defaultdict(lambda: Cars(fees))
    for record in records:
        time, carNum, inout = record.split()
        carsDict[carNum].update(inout, time)
    return [v.getMoney() for k, v in sorted(carsDict.items())]
