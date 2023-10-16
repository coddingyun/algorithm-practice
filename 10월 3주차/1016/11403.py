import sys
input = sys.stdin.readline

n = int(input())
INF = int(1e9)

dp = [[INF]*n for _ in range(n)]

for i in range(n):
  graph = list(map(int, input().split()))
  for j in range(n):
    if graph[j] == 1:
      dp[i][j] = 1

for k in range(n):
  for i in range(n):
    for j in range(n):
      dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(n):
  for j in range(n):
    if dp[i][j] != INF:
      print(1, end=" ")
    else:
      print(0, end=" ")
  print()
