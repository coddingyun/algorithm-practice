from collections import deque
import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

queue = deque([])
queue.append([0,0])

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


INT_MAX = int(1e9)
answer = INT_MAX

visited = [[False]*m for _ in range(n)]
visited[0][0] = 1

while queue:
  nx, ny = queue.popleft()
  if nx == n-1 and ny == m-1:
    answer = min(answer, visited[nx][ny]-1)
  if graph[nx][ny] == 2:
    answer = min(answer, visited[nx][ny]+(n-1)-nx+(m-1)-ny-1)
  for i in range(4):
    rx = nx + dx[i]
    ry = ny + dy[i]
    if 0<=rx<n and 0<=ry<m and visited[rx][ry] == 0:
      if graph[rx][ry] != 1:
        queue.append([rx, ry])
        visited[rx][ry] = visited[nx][ny] +1

if answer == INT_MAX or answer > t:
  print('Fail')
else: print(answer)
