## 첫시도
```
from collections import deque
import copy

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

s, e = map(int, input().split())

for i in range(n+1):
  graph[i].sort()

visited = [[False]*(n+1) for _ in range(n+1)]
queue = deque([[s, 0, [s]]])

answer = 0

while queue:
  nx, ncount, nq = queue.popleft()
  if nx == e:
    for i in range(len(nq)-1):
      visited[nq[i]][nq[i+1]] = True
      visited[nq[i+1]][nq[i]] = True
    answer += ncount
    break
  for item in graph[nx]:
    if item not in nq:
      tq = copy.deepcopy(nq)
      tq.append(item)
      queue.append([item, ncount+1, tq])


reverseQueue = deque([[e, 0, [e]]])

while reverseQueue:
  nx, ncount, nq = reverseQueue.popleft()
  if nx == s:
    answer += ncount
  for item in graph[nx]:
    if item not in nq and visited[nx][item] == False:
      tq = copy.deepcopy(nq)
      tq.append(item)
      reverseQueue.append([item, ncount+1, tq])
```
bfs 시간복잡도 O(정점수+간선수) <br/>
item not in nq를 했으니까 N이 곱해질 것이다 (nq의 최대길이는 N이니까) <br/>
거기에다 deepcopy 때문에 N이 곱해지면서 O(N+MNN)

## 두번째 시도
```
nq.append(item)
queue.append([item, ncount+1, nq])
nq.pop()
```
deepcopy를 제거하였지만 여전히 시간초과 <br/>
item not in nq 해결을 안했으니까 O(N+MN)

### *참고
```
nq.append(item)
queue.append([item, ncount+1, nq])
nq.pop()
```
이렇게 하면 nq.pop이 된 상태의 nq가 queue에 들어가게 된다. <br/>
왜냐하면 원본 리스트의 참조가 추가되기 때문이다. 조심할것!!

## 세번째 시도 (정답)

```
while queue:
  #print(queue)
  nx, ncount, nq = queue.popleft()
  if nx == e:
    for i in range(len(visited)):
      visited[i] = 0
    for i in range(1, len(nq)):
      visited[nq[i]] = 2
    answer += ncount
    break
  for item in graph[nx]:
    if visited[item] == 0:
      visited[item] = 1
      queue.append([item, ncount+1, nq+[item]])
```
그냥 전체적으로 방문처리해도 ok. <br/>
완벽히는 이해 못하겠지만 최단거리로 간다면 다시 돌아올일은 없음 (직접 적어보면 어렴풋이 알수 있음)<br/>
O(N+M)

## 정리
1. 사전 순으로 출력하라.
   ```
   for i in range(n):
     graph[i].sort()
   ```

2. 최단 거리는 bfs로 해결해야한다.
   count가 작은 순으로 queue에 쌓이게 되니까
3. copy.deepcopy를 쓰지 않는 방법을 모색하자.
   - 이문제에서는 nq+[item]
