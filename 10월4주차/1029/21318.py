import sys
input = sys.stdin.readline

n = int(input())

level = list(map(int, input().split()))

q = int(input())

dp = []

for i in range(len(level)-1):
  if level[i] > level[i+1]:
    dp.append(1)
  else:
    dp.append(0)
dp.append(0)

sumDp = [0]*(len(dp))
sumDp[0] = dp[0]

for i in range(1, len(dp)):
  sumDp[i] = sumDp[i-1] + dp[i]

for _ in range(q):
  x, y = map(int, input().split())
  if x == 1 and y == 1:
    print(0)
  elif x == 1:
    print(sumDp[y-2])
  else:
    print(sumDp[y-2]-sumDp[x-2])
