import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dp = [[0]*m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      dp[i][j] = 1
      
for i in range(1, n):
  for j in range(1, m):
    if graph[i][j] == 1:
      dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1

answer = max(map(max, dp))
print(answer*answer)
