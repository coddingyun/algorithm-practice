from collections import deque

graph = []

for _ in range(8):
  graph.append(list(input()))

def move_walls(graph, line, x, y):
  tgraph = [['.']*8 for _ in range(8)]
  for i in range(8):
    for j in range(8):
      if graph[i][j] == '#':
        tgraph[i][j] = '.'
        if i<8-line:
          if i+line == x and j == y:
            return False
          else:
            tgraph[i+line][j] = '#'
  return tgraph

visited = [[[False]*64 for _ in range(8)] for _ in range(8)]
queue = deque()
queue.append([7, 0, 0])

visited[7][0][0] = True

dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
answer = 0

while queue:
  nx, ny, nline = queue.popleft()
  if nx == 0 and ny == 7:
    answer = 1
    break
  tgraph = move_walls(graph, nline+1, nx, ny)
  if tgraph:
    queue.append([nx, ny, nline+1])
    visited[nx][ny][nline+1] = True

  for i in range(8):
    tx = nx + dx[i]
    ty = ny + dy[i]
    tgraph = move_walls(graph, nline, tx, ty)

    if 0<=tx<8 and 0<=ty<8 and tgraph and tgraph[tx][ty] == '.' and visited[tx][ty][nline+1] == False:
      agraph = move_walls(graph, nline+1, tx, ty)
      if agraph:
        visited[tx][ty][nline+1] = True
        queue.append([tx, ty, nline+1])
  
print(answer)
