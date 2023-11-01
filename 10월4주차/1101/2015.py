from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = list(map(int, input().split()))

dp = [0]
answer = 0

for i in range(n):
  dp.append(dp[-1]+nums[i])

idx_dict = defaultdict(list)

for i in range(n, 0, -1):
  sum = dp[i]
  if sum == k:
    answer += 1
  target = sum + k
  answer += len(idx_dict[target])
  idx_dict[sum].append(i)

print(answer)
