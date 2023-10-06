import sys

input = sys.stdin.readline

n = int(input())
arr = [-1]
arr.extend(list(map(int, input().split())))

dp = [[0 for i in range(20+1)] for j in range(100+1)]  # dp[i][j] = i번째에서 j가 되는 경우의 수 1<=i<=100, 0=<j<=20
dp[1][arr[1]] += 1

for i in range(2, n):
    for j in range(20+1):
        if dp[i-1][j]:
            if j+arr[i] <= 20:
                dp[i][j+arr[i]] += dp[i-1][j]
            if j-arr[i] >= 0:
                dp[i][j-arr[i]] += dp[i-1][j]


print(dp[n-1][arr[-1]])
