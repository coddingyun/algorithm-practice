## Intro
처음에 무슨 dp[1][1][3][2] 이렇게 만들어야 하나 이상한 생각에 빠져서 점화식을 못만들었음
키워드 보니까 누적합이길래 누적합 구글링해서 검색해봄
완전 누적합 문제구나 해서 열심히 풀음

## 첫번째 시도: 1차원 누적합
```python
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
 graph.append(list(map(int, input().split())))

dp = [[0]*m for _ in range(n)]

for i in range(n):
  dp[i][0] = graph[i][0]

for i in range(n):
  for j in range(1, m):
    dp[i][j] = dp[i][j-1] + graph[i][j]
    

k = int(input())

for _ in range(k):
  sx, sy, ex, ey = map(int, input().split())
  sx -= 1
  sy -= 1
  ex -= 1
  ey -= 1
  answer = 0
  for i in range(sx, ex+1):
    answer += dp[i][ey]
  if sy>0:
    for j in range(sx, ex+1):
      answer -= dp[j][sy-1]
```

처음에 1차원으로만 누적합 계산했음. 그랬더니 pypy3에서만 정답 처리됌. 왜 그랬는지 몰랐는데 지금 보니까 k값이 엄청크다.. 그래서 안됐네

## 두번째 시도: 2차원 누적합
결국 구글링 ㅎ

[이분](https://my-coding-notes.tistory.com/237) 너무 잘 설명해주심 참고해서 원래 내 코드에 입혔음

```python
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
```
