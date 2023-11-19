import heapq

INF = int(1e9)
            
def solution(n, paths, gates, summits):
    summits.sort()
    answer = []
    resultArr = []
    graph = [[] for _ in range(n+1)]
    for path in paths:
        i, j, w = path
        graph[i].append((j, w))
        graph[j].append((i, w))
    q = []
    dist = [INF]*(n+1)
    for gate in gates:
        dist[gate] = 0 
        for i, w in graph[gate]:
            heapq.heappush(q, (w, i))
            
    while q:
        cost, v = heapq.heappop(q)
        if dist[v] <= cost:
            continue
        dist[v] = cost
        if v in summits:
            continue
        for nv, ncost in graph[v]:
            if dist[nv] > cost:
                heapq.heappush(q, (max(cost, ncost), nv))
    
    answerNum, answerCnt = 0, INF
    for summit in summits:
        if dist[summit] < answerCnt:
            answerNum = summit
            answerCnt = dist[summit]
    answer = [answerNum, answerCnt]
    return answer
