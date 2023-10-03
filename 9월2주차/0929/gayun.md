## 풀이방법
1. visited
   ```
   visited = [[[False]*64 for _ in range(8)] for _ in range(8)]
   ```
   x값, y값, 벽의 이동횟수를 담았다. 왜냐하면 벽이 이동함에 따라 x,y 좌표에 다시 방문이 가능하기 때문이다.
2. bfs
   ```
   while queue:
    nx, ny, nline = queue.popleft()
    if nx == 0 and ny == 7: # 도착시 break
      answer = 1
      break
    tgraph = move_walls(graph, nline+1, nx, ny) # 제자리 이동
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
   ```
  bfs로 전체를 돌면서 가능한 경우만 queue에 담는다.
3. move_walls
  ```
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
  ```
  큐에 벽이 몇번 아래로 내려갔는지를 저장해두었으므로 그 값을 받아와서 벽을 이동시켜준다. 불가능하면 False를 return 하고 가능하면 이동한 graph를 return 한다.
