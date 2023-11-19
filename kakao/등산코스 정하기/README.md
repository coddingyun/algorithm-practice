## 첫 시도

```python
import heapq
import sys
sys.setrecursionlimit(10**9)

def dfs(v, graph, visited, summits, gates, maxVal, resultArr):
    if v in summits:
        heapq.heappush(resultArr, (maxVal, v))
        return
    visited[v] = True
    while graph[v]:
        w, i = heapq.heappop(graph[v])
        if i in gates:
            continue
        if visited[i] == False and i not in gates:
            nextVal = max(maxVal, w)
            dfs(i, graph, visited, summits, gates, nextVal, resultArr)
            

def solution(n, paths, gates, summits):
    answer = []
    resultArr = []
    graph = [[] for _ in range(n+1)]
    for path in paths:
        i, j, w = path
        heapq.heappush(graph[i], (w, j))
        heapq.heappush(graph[j], (w, i))
    for gate in gates:
        visited = [False] * (n+1)
        subGraph = [arr[:] for arr in graph]
        dfs(gate, subGraph, visited, summits, gates, 0, resultArr)
        
    answerCnt, answerNum = heapq.heappop(resultArr)
    answer = [answerNum, answerCnt]
    return answer
```

시간초과 + 틀림

## 정답 참고
```python
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
```
다익스트라 응용..
[참고](https://school.programmers.co.kr/questions/35438)
