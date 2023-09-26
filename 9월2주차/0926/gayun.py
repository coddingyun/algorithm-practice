import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())

graph = []

for _ in range(m):
  graph.append(list(map(int, input().split())))


edx = [-1, 1, 0, 0, 1, -1]
edy = [0, 0, -1, 1, 1, 1]

odx = [-1, 1, 0, 0, -1, 1]
ody = [0, 0, 1, -1, -1, -1]

visited = [[0]*n for _ in range(m)]

total = 0

def dfs(visited, x, y):
  global total
  visited[x][y] = 1
  nearNum = 0
  for i in range(6):
    if x % 2 ==0:
      nx = x + edx[i]
      ny = y + edy[i]
    else:
      nx = x + odx[i]
      ny = y + ody[i]
    if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
      nearNum += 1
      if visited[nx][ny] == 0:
        dfs(visited, nx, ny)
  total += (6 - nearNum)

total2 = 0
  
def dfs2(visited, x, y, arr):
  global total2
  visited[x][y] = 1
  arr.append([x, y])
  nearNum = 0
  for i in range(6):
    if x % 2 ==0:
      nx = x + edx[i]
      ny = y + edy[i]
    else:
      nx = x + odx[i]
      ny = y + ody[i]
    if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 0:
      nearNum += 1
      if visited[nx][ny] == 0:
        dfs2(visited, nx, ny, arr)
  total2 += (6 - nearNum)

for i in range(m):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == 0:
      dfs(visited, i, j)

for i in range(m):
  for j in range(n):
    if graph[i][j] == 0 and visited[i][j] == 0:
      arr = []
      total2 = 0
      dfs2(visited, i, j, arr)
      flag = False
      for item in arr:
        if item[0] ==0 or item[0] == m-1 or item[1] == 0 or item[1] == n-1:
          flag = True
          break
        else:
          pass
      if flag == False:
        total -= total2
      
print(total)
