# 시행착오
- 처음에는 dp[x1][y2][x2][y2] 이런식의 4차원 배열을 만들어서 풀려고 했음
- 그러나 1 ≤ N, M ≤ 1,024 조건을 보고 대략 1000^4 개의 메모리가 필요하다는 것을 보고 바로 포기함
- K(1 ≤ K ≤ 100,000)이므로 O(KNM)>=100,000 * 1,000 * 1,000 이기 때문에 NM을 1로 만들어야 풀이가 가능함
# 아이디어
- K번 반복할때마다 O(1)으로 동작하게 해야하므로 각 포인트(x1,y1,x2,y2)를 이용해서 dp 점화식을 세우고자 노력함
- dp[x][y]를 (0,0) <-> (x,y)까지의 사각형 전체 누적합으로 정의하고,
- 실제 구하고자하는 교집합 직사각형 영역을 바로구하기보다 영역들의 덧셈 뺄셈으로 구했음
- 예) (x1,y1)(x2,y2) 영역 = -(직사각형 바깥영역들)+(바깥영역들의 교집합) =-(A+B)+C = -(dp[x2][y1-1]+dp[x1-1][y2])+dp[x1-1][y1-1]
# 마무리
- input = sys.stdin.readline은 꼭 써주자!
- dp table 정의
```python
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

```
- 직사각형 영역 구하기
```python
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

```
