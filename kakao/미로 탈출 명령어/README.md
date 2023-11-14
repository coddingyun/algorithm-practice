### 첫시도
```python
import sys
sys.setrecursionlimit(10**9)

dx = [1,0,0,-1]
dy = [0,-1,1,0]
value = ['d', 'l', 'r', 'u']
possible = False
answer = ''

def findPath(n, m, x, y, r, c, k, result, curK):
    global possible, answer
    if possible:
        return
    if curK == k:
        if x == r and y == c:
            possible = True
            answer = result
        return
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= m:
            findPath(n, m, nx, ny, r, c, k, result+value[i], curK+1)


def solution(n, m, x, y, r, c, k):
    global possilbe, answer
    if (abs(x-r)+abs(y-c)+k)%2==1:
        return "impossible"
    findPath(n, m, x, y, r, c, k, "", 0)
    return answer
```
6개 통과
### 두번째 시도
```python
import sys
from itertools import permutations
sys.setrecursionlimit(10**9)

dx = [1,0,0,-1]
dy = [0,-1,1,0]
value = ['d', 'l', 'r', 'u']

            
def checkPossible(path, x, y, n, m):
    result = ""
    for index in path:
        x += dx[index]
        y += dy[index]
        if 1 <= x <= n and 1 <= y <= m:
            result += value[index]
        else:
            return False
    
    return result

def solution(n, m, x, y, r, c, k):
    global possilbe
    answer = []
    necessaryPath = []
    diffX = x-r
    diffY = y-c
    absDiffX = abs(diffX)
    absDiffY = abs(diffY)
    if (absDiffX+absDiffY+k)%2==1:
        return "impossible"
    setNumber = (k-absDiffX-absDiffY)//2
    if diffX>0:
        necessaryPath+=[3]*absDiffX
    else:
        necessaryPath+=[0]*absDiffX
    if diffY>0:
        necessaryPath+=[1]*absDiffY
    else:
        necessaryPath+=[2]*absDiffY
    for i in range(setNumber+1):
        candidatePath = necessaryPath[:]
        candidatePath+=[0, 3]*i
        candidatePath+=[1, 2]*(setNumber-i)
        permuArr = list(set(permutations(candidatePath, len(candidatePath))))
        for item in permuArr:
            result = checkPossible(item, x, y, n, m)
            if result != False:
                answer.append(result)
    if len(answer) == 0:
        return "impossible"
    answer.sort()           
    return answer[0]
```
7개 통과

### 세번째 시도
질문하기 게시글을 참고하였다. 오히려 첫번째 시도가 정답과 가까웠다. <br/>
조건을 잘 명시하면, 굳이 모든 d,l,r,u를 돌 필요없이 바로 break를 걸어주면 된다. 왜냐면 d,l,r,u가 이미 사전순이기 때문이다. <br/>
이때 조건은 현재 계산한 값에서 k보다 남은 최소 거리가 더 크면 더이상 가지 않는 조건이다.
