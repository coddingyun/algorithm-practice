import heapq
from collections import deque

q = []

def dfs(info, result, curIdx, n):
    curSum = sum(result[1:])
    if curIdx == 11:
        if n - curSum >= 0 and result[0] > 0:
            #result[0] -= result[0]*2
            result[1] += (n - curSum)
            result = list(map(lambda x: -x, result))
            heapq.heappush(q, result)
        return
    apeach = info[curIdx]
    if n - curSum > apeach:
        aresult = result[:]
        aresult[11-curIdx] = apeach + 1
        aresult[0] += (10-curIdx)
        dfs(info, aresult, curIdx+1, n)
    bresult = result[:]
    if apeach != 0:
        bresult[0] -= (10-curIdx)
    dfs(info, bresult, curIdx+1, n)

def solution(n, info):
    dfs(info, [0]*12, 0, n)
    if len(q) == 0:
        return [-1]
    result = heapq.heappop(q)
    result = list(map(lambda x: -x, result[1:]))
    result.reverse()
    return result
