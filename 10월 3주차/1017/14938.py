import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, r = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

items = [0] + list(map(int, input().split()))

itemsSum = [0]*(n+1)

for _ in range(r):
  a, b, t = map(int, input().split())
  graph[a][b] = t
  graph[b][a] = t

for k in range(1, n+1):
  graph[k][k] = 0
  for i in range(1, n+1):
    visited = set()
    itemsCnt = 0
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
      if graph[i][j] <= m and j not in visited:
        visited.add(j)
        itemsCnt += items[j]
    itemsSum[i] = itemsCnt

print(max(itemsSum))
