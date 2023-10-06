import sys
input = sys.stdin.readline

n = int(input())

number = list(map(int, input().split()))

dp = [[0]*101 for _ in range(21)]

dp[number[0]][1] = 1

for i in range(1, n-1):
  for j in range(0, 21):
    if dp[j][i] > 0:
      if 0 <= j + number[i] <= 20:
        dp[j+number[i]][i+1] += (dp[j][i])
      if 0 <= j - number[i] <= 20:
        dp[j-number[i]][i+1] += (dp[j][i])

print(dp[number[-1]][len(number)-1])
