## 맞왜틀!?
```
from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

queue = deque([])
queue.append([0,0,0,0])

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


INT_MAX = int(1e9)
answer = INT_MAX

visited = [[False]*m for _ in range(n)]
visited[0][0] = True

while queue:
  nx, ny, nt, gram = queue.popleft()
  if nx == n-1 and ny == m-1:
    if nt<=t:
      answer = min(answer, nt)
  for i in range(4):
    rx = nx + dx[i]
    ry = ny + dy[i]
    if 0<=rx<n and 0<=ry<m and visited[rx][ry] == False:
      if graph[rx][ry] == 2:
        queue.append([rx, ry, nt+1, 1])
        visited[rx][ry] = True
      elif graph[rx][ry] == 1 and gram == 1:
        queue.append([rx, ry, nt+1, 1])
        visited[rx][ry] = True
      elif graph[rx][ry] == 0:
        queue.append([rx, ry, nt+1, gram])
        visited[rx][ry] = True

if answer == INT_MAX:
  print('Fail')
else: print(answer)
```
16%에서 틀렸습니다. gram이 있는 경우에는 벽 부수면서도 가고 그냥 가기도 하고 모든 경우를 커버하는데 왜 틀릴까 ? 질문게시판에 나랑 똑같이 푼사람이 한명 있었는데 답변은 없다 ㅜ

그래서 구글링해서 힌트 얻음 -> 그람을 얻는 경우에는 벽을 다 부수고 갈 수 있으니까 그람을 얻은 이후에는 최단 거리를 하면 된다.
```
if graph[nx][ny] == 2:
    answer = min(answer, visited[nx][ny]+(n-1)-nx+(m-1)-ny-1)
```
