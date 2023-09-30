# 시간초과 풀이
```python
import sys
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
visit = [0 for i in range(n+1)]
min_dist = 100000
min_route = deque([])
answer = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
s, e = map(int, input().split())
for i in range(n):
    graph[i].sort()


def dfs(cur, depth, tar, route):
    global min_route, min_dist
    visit[cur] = 1

    if cur == tar:
        if min_dist > depth:
            min_dist = depth
            min_route.clear()
            for v in route:
                min_route.append(v)

    else:
        for nxt in graph[cur]:
            if visit[nxt] == 0:
                route.append(nxt)
                dfs(nxt, depth+1, tar, route)
                visit[nxt] = 0
                route.pop()


dfs(s, 0, e, deque([]))
answer += min_dist
while min_route:
    node = min_route.popleft()
    visit[node] = 1
visit[s] = 0
visit[e] = 0
min_dist = 100000
dfs(e,0, s, deque([]))
answer += min_dist
print(answer)
```
# O(M)
# 회고
- [2000ms 로 1초가 넘었는데 맞았다고 뜨는 이유](https://help.acmicpc.net/language/info)
- [다른 사람들의 풀이를 보니 python으로도 100ms 대의 풀이가 존재](https://www.acmicpc.net/problem/status/22868/1003/1)
- 내 풀이는 왜 느린가?
