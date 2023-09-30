# 시간초과 풀이
- 처음에는 dfs로 가능한 모든 경로를 체크했음
- 이렇게 되면 방문했던 노드도 다시 또 방문할 수 있으므로시간 복잡도가 O(NM)이 되어 NxM >= 50억
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
- 결국에는 최소거리를 어떻게 측정하고, 그때의 최소경로 노드를 어떻게 저장할 건지가 핵심이였음 
- 이번에는 BFS의 depth 개념으로 출발지-목적지 최소거리를 구하고 => O(M), 역으로 최소경로를 구하고 => O(M) , 다시 목적지-출발지 최소거리를 구해서 => O(M)
- O(M)으로 풀이를 진행했음 
  ```python
    from collections import deque
    
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    answer = 0
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, e = map(int, input().split())
    for i in range(n):
        graph[i].sort()
    
    queue = deque([s])
    visit[s] = 1
    
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visit[nxt] == 0:
                queue.append(nxt)
                visit[nxt] = 1
                dist[nxt] = dist[cur] + 1
    
    
    visit = [0 for _ in range(n+1)]
    queue = deque([e])
    visit[e] = 1
    while queue:
        cur = queue.popleft()
        if cur == s:
            continue
        min_dist = 100000
        min_node = 0
        for nxt in graph[cur]:
            if min_dist > dist[nxt]:
                min_dist = dist[nxt]
                min_node = nxt
        visit[min_node] = 1
        queue.append(min_node)
    
    answer += dist[e]
    
    visit[e] = 0
    visit[s] = 0
    
    dist = [0 for _ in range(n+1)]
    queue = deque([e])
    visit[e] = 1
    
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visit[nxt] == 0:
                queue.append(nxt)
                visit[nxt] = 1
                dist[nxt] = dist[cur] + 1

    answer += dist[s]
  ```
# 회고
- [2000ms 로 1초가 넘었는데 맞았다고 뜨는 이유](https://help.acmicpc.net/language/info)
- [다른 사람들의 풀이를 보니 python으로도 100ms 대의 풀이가 존재](https://www.acmicpc.net/problem/status/22868/1003/1)
- 내 풀이는 왜 느린가?
```python
input = sys.stdin.readline
```
- 이 한줄을 추가했더니 2220 ms -> 148 ms 10배 이상 빨라짐
- 그 이유는?
    - input과 sys.stdin.readline은 구현 디테일이 다르기 때문임
    - 첫째, input에는 프롬프트(예, 나이를 입력하세요: )를 입력 전에 표시할 수 있기 때문에 프롬프트가 없더라도 디폴트로 오버헤드가 발생
    - 둘째, input은 개행문자를 제거하고, sys.stdin.readline은 개행문자를 제거하지 않음
        -  이 문제와 같이, 문자열을 입력받는게 아니라 숫자를 취급하는 문제는 크게 신경쓸 필요 없음
        - 하지만 문자열을 처리해야 하는 문제의 경우 sys.stdin.readline을 통해 얻은 끝 문자는 제거해줘야 한다는 점을 기억해야함
        -  it may be faster to let "input()" do it for you, rather than doing sys.stdin.readline().strip()
- [input() vs sys.stdin.readlin()](https://stackoverflow.com/questions/22623528/sys-stdin-readline-and-input-which-one-is-faster-when-reading-lines-of-inpu)
