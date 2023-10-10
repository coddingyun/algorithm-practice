import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
dp = [1]*(n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

for i in range(1, n+1):
  for item in graph[i]:
    dp[i] = max(dp[i], 1+dp[item])

for i in range(1, n+1):
  print(dp[i])
