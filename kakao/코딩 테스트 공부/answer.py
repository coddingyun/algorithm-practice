INF = int(1e9)

def solution(alp, cop, problems):
    answer = 0
    rAlp , rCop = 0, 0

    for item in problems:
        rAlp = max(item[0], rAlp)
        rCop = max(item[1], rCop)
    alp = min(alp,rAlp)
    cop = min(cop,rCop)

    dp = [[INF]*(rCop+1) for _ in range(rAlp+1)]
    dp[alp][cop] = 0
    for i in range(alp, rAlp+1):
        for j in range(cop, rCop+1):
            if i+1 <= rAlp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j+1 <= rCop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            for [a, b, c, d, e] in problems:
                if i>=a and j>=b:
                    row, col = 0, 0
                    if i+c > rAlp:
                        row = rAlp
                    else:
                        row = i+c
                    if j+d > rCop:
                        col = rCop
                    else:
                        col = j+d
                    dp[row][col] = min(dp[row][col], dp[i][j] + e)
    return dp[rAlp][rCop]
