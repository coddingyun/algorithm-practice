import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())

graph = [[[INF]*(2) for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = [c, b]
  graph[b][a] = [c, a]

for k in range(1, n+1):
  graph[k][k][0] = 0
  for i in range(1, n+1):
    for j in range(1, n+1):
      newVal = graph[i][k][0] + graph[k][j][0]
      if newVal < graph[i][j][0]:
        graph[i][j][0] = newVal
        graph[i][j][1] = graph[i][k][1]

for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      print('-', end=" ")
    else:
      print(graph[i][j][1], end=" ")
  print()
