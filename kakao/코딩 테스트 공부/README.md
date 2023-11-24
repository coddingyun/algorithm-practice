## 첫번째 시도
dp 느낌이 나서 그 느낌으로 풀었다.
```python
import heapq

INF = int(1e9)

def solution(alp, cop, problems):
    answer = 0
    q = []
    rAlp , rCop = 0, 0

    for item in problems:
        rAlp = max(item[0], rAlp)
        rCop = max(item[1], rCop)

    dp = [[INF]*(151) for _ in range(151)]
    dp[alp][cop] = 0
    for i in range(alp, 151):
        for j in range(cop, 151):
            dp[i][j] = min(dp[i][j], dp[i-1][j]+1)
            dp[i][j] = min(dp[i][j], dp[i][j-1]+1)
            for [a, b, c, d, e] in problems:
                if i-c>=a and j-d>=b:
                    dp[i][j] = min(dp[i][j], dp[i-c][j-d] + e)
            if i>=rAlp and j>=rCop and dp[i][j] != INF:
                heapq.heappush(q, dp[i][j])
    answer = heapq.heappop(q)
    return answer
```
but.. 이 경우 i와 j가 rAlp와 rCop보다 큰 경우에서 최소 값이 나올 수도 있다.. 그래서 배열의 크기를 점점 키웠는데 그러다보니 효율성 부문에서 시간초과,,

## 두번째 시도
```python
import heapq

INF = int(1e9)

def solution(alp, cop, problems):
    answer = 0
    q = []
    rAlp , rCop = 0, 0

    for item in problems:
        rAlp = max(item[0], rAlp)
        rCop = max(item[1], rCop)

    dp = [[INF]*(rCop*2+1) for _ in range(rAlp*2+1)]
    dp[alp][cop] = 0
    for i in range(alp, rAlp):
        for j in range(cop, rCop):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
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
```
자꾸 두번째 예제에서 다른 값이 나왔다... 결국 [참고](https://school.programmers.co.kr/questions/35405)


## 정답
```python
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
```

뭔가 어디까지 배열을 돌고.. 어디서 부터 시작하고 이런게 중요한 거 같다.

rAlp, rCop까지 dp를 도는 게 아니라 rAlp+1, rCop+1까지 도는 이유는 dp[i+1][j]나 dp[i][j+1]에서 j나 i값에는 rCop나 rAlp도 들어갈 수 있기 때문이다.

그리고 alp = min(alp,rAlp) cop = min(cop,rCop) 이걸 해주는 이유는 최대값이 기존 가지고 있는 알고력, 코딩력보다 낮은 경우에는 무조건 0을 뱉어야 하기 때문!!

따로 조건으로 return하지 않고 저렇게 한 이유는.. 하나만 작을 수 있으니까 그경우에는 또 for문을 돌아야 한다.

## 비고
올리지 않은 한문제까지 포함하여 총 12개의 카카오 코테 문제를 풀었다. 목표치에 달성은 하지 못했지만, 백준도 3문제 정도 풀었으니 그래도 열심히 풀었다..!

lv2까지는 괜찮은데 lv3부터는 쉽지 않다. 거의 항상 해설을 참고했던 것 같다. 코테 컷을 넘기려면 lv3는 풀 수 있어야 안전하다고 하던데 걱정이 된다.

내일 카카오 코테인데 열심히 해보장...
