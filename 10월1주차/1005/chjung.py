import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []
dp = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if (i - 1 < 0) or (j - 1 < 0):
            if (i - 1 < 0) and (j - 1 < 0):
                dp[i][j] = matrix[i][j]
            elif i - 1 < 0:
                dp[i][j] = dp[i][j - 1] + matrix[i][j]
            else:
                dp[i][j] = dp[i - 1][j] + matrix[i][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i][j]


k = int(input())
answer = []
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    if (x1 - 1 < 0) or (y1 - 1 < 0):
        if (x1 - 1 < 0) and (y1 - 1 < 0):
            answer.append(dp[x2][y2])
        elif x1 - 1 < 0:
            answer.append(dp[x2][y2] - dp[x2][y1-1])
        else:
            answer.append(dp[x2][y2] - dp[x1-1][y2])
    else:
        answer.append(dp[x2][y2]-(dp[x2][y1-1]+dp[x1-1][y2])+dp[x1-1][y1-1])

for ans in answer:
    print(ans)
