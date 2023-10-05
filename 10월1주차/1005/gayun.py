import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
 graph.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]

for i in range(n):
  for j in range(m):
    dp[i][j] = graph[i][j]
    if i > 0:
      dp[i][j] += dp[i-1][j]
    if j > 0:
      dp[i][j] += dp[i][j-1]
    if i>0 and j>0:
      dp[i][j] -= dp[i-1][j-1]
    
k = int(input())

for _ in range(k):
  sx, sy, ex, ey = map(int, input().split())
  sx -= 1
  sy -= 1
  ex -= 1
  ey -= 1
  answer = 0
  answer += dp[ex][ey]
  if sy>0:
    answer -= dp[ex][sy-1]
  if sx>0:
    answer -= dp[sx-1][ey]
  if sx > 0 and sy > 0:
    answer += dp[sx-1][sy-1]
  print(answer)
