import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
m = int(input())

dp = [[False]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  dp[i][1] = True

for i in range(1, n):
  dp[i][2] = arr[i] == arr[i+1]

for j in range(3, n+1):
  for i in range(1, n):
    if j-2 <= n and i+j-1 <= n and i <= n:
      dp[i][j] = dp[i+1][j-2] and arr[i] == arr[i+j-1]
  
for _ in range(m):
  s, e = map(int, input().split())
  print(int(dp[s][e-s+1]))
