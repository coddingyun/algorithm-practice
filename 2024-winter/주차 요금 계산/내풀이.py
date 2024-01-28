import math

def calMin(time):
    timeArr = time.split(':')
    result = int(timeArr[0])*60 + int(timeArr[1])
    return result;

def solution(fees, records):
    answer = []
    preAns = []
    final = [0]*10000
    cars = [-1]*10000
    for record in records:
        recordArr = record.split(" ")
        if recordArr[2] == 'IN':
            cars[int(recordArr[1])] = calMin(recordArr[0])
        else:
            result = calMin(recordArr[0]) - cars[int(recordArr[1])]
            cars[int(recordArr[1])] = -1
            final[int(recordArr[1])] += result
    for idx, item in enumerate(cars):
        if item !=-1:
            result = calMin('23:59') - item
            final[idx] += result
    for item in final:
        if item !=0:
            money = fees[1]
            if item > fees[0]:
                money += math.ceil((item-fees[0])/fees[2]) * fees[3]
            answer.append(money)

    return answer
