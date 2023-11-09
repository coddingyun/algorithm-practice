def findFarDelivery(pickups, deliveries, cap, lastIdx):
    for i in range(lastIdx, -1, -1):
        if deliveries[i] > 0 or pickups[i] > 0:
            return i
    return -1

def doDelivery(deliveries, pickups, idx, cap):
    totalDelivery = 0
    totalPickUp = 0
    flagDelivery = False
    flagPickUp = False
    Dindex = idx
    Pindex = idx
    for i in range(idx, -1, -1):
        if deliveries[i] > 0 and flagDelivery == False:
            totalDelivery += deliveries[i]
            if totalDelivery < cap:
                deliveries[i] = 0
            elif totalDelivery == cap:
                deliveries[i] = 0
                flagDelivery = True
                Dindex = i-1
            else:
                deliveries[i] = totalDelivery - cap
                flagDelivery = True
                Dindex = i
        if pickups[i] > 0 and flagPickUp == False:
            totalPickUp += pickups[i]
            if totalPickUp <= cap:
                pickups[i] = 0
            elif totalPickUp == cap:
                pickups[i] = 0
                flagPickUp = True
                Pindex = i-1
            else:
                pickups[i] = totalPickUp - cap
                flagPickUp = True
                Pindex = i
        if flagPickUp and flagDelivery:
            break
    return max(Dindex, Pindex)


def solution(cap, n, deliveries, pickups):
    answer = 0
    lastIdx = n-1
    while True:
        idx = findFarDelivery(pickups, deliveries, cap, lastIdx)
        if idx == -1: break
        lastIdx = doDelivery(deliveries, pickups, idx, cap)
        answer += (idx+1)*2

    return answer
