### 점화식
> dp[i] = max(dp[i의 선수과목] + 1)

선수과목 조건이 A < B 이기 때문에 항상 i > i의 선수과목이므로 바텀업 방식으로 dp 구현 가능

### 시간초과
input = sys.stdin.readline 안하면 시간초과 남!
