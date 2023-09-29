# 14%
- dist 배열을 시간처럼 사용, dist = 1 -> 1초후 움직일 수 있는 곳
- 이렇게 하면 최단거리를 구할 수 있지만, 이 문제에서는 최단거리를 구하는 게 아니라 제자리에 있는 것을 포함해서 벽돌을 피해 도착할 수 있는지가 관건임
- 따라서 이렇게 하면 안됨
```python
from collections import deque

matrix = []
blocks = deque([])
new_blocks = deque([])
visit = [[0 for i in range(8)] for j in range(8)]
dist = [[0 for i in range(8)] for j in range(8)]
dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]
for i in range(8):
    line = list(input())
    for j in range(8):
        if line[j] == '#':
            blocks.append((i, j))
    matrix.append(line)



queue = deque([(7, 0)])
cnt = 0
while queue:

    cur = queue.popleft()

    if cnt < dist[cur[0]][cur[1]]:
        cnt += 1
        while blocks:
            block = blocks.popleft()
            matrix[block[0]][block[1]] = '.'
            if block[0] + 1 <= 7:
                new_blocks.append((block[0]+1, block[1]))
                matrix[block[0]+1][block[1]] = '#'
        while new_blocks:
            blocks.append(new_blocks.popleft())
    if matrix[cur[0]][cur[1]] == '#':
        continue
    for i in range(8):
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8:
            continue
        if visit[nx][ny] == 0 and matrix[nx][ny] == '.':
            queue.append((nx, ny))
            visit[nx][ny] = 1
            dist[nx][ny] += dist[cur[0]][cur[1]] + 1

```
# 100%
- 제자리에 있는 방향을 dx, dy에 추가
  ```python
  dx = [0, 1, 0, -1, 1, 1, -1, -1, 0]
  dy = [1, 0, -1, 0, -1, 1, -1, 1, 0]
  ```
- 방문 배열에 "시간" 차원을 추가해서 t초에 x,y에 방문했는지를 확인하였음
  ```python
  visit = [[[0 for i in range(8)] for j in range(8)] for j in range(100)]
  ```
- 이럴 경우 무한히 큐가 추가될 수 있으므로, 8x8 바둑판에서 최대 시간을 대략적으로 100초로 잡고 100이상 넘어가는 시간은 큐에 담지 않게하였음
  ```python
      for i in range(9):
          nt = cur[0] + 1
          nx = cur[1] + dx[i]
          ny = cur[2] + dy[i]
  
          if nx < 0 or nx >= 8 or ny < 0 or ny >= 8 or nt >= 100:
              continue
  
          if visit[nt][nx][ny] == 0 and matrix[nx][ny] == '.':
              queue.append((nt, nx, ny))
              visit[nt][nx][ny] = 1
  ```
