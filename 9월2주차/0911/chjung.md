# 요약
- queue를 구현할 때 리스트가 아닌 "deque"를 쓰자 [https://wellsw.tistory.com/122]
- Python3 와 Pypi3는 채점 속도가 다르다 [https://www.acmicpc.net/board/view/87198]
  
# 설명
- deque은 내부적으로 double-linked list로 구현되어 있습니다.
그래서 양 끝의 요소의 추가/삭제가 O(1)을 만족하게됩니다.
- list는 fixed size memory blocks(array)로 구현되어 있습니다.
이름은 List여서 링크드 리스트처럼 보이지만 **고정된 사이즈의 메모리를 갖는 array** 형태입니다.
리스트의 마지막 원소를 삭제는 O(1)이지만, 첫번째 원소를 삭제하면 삭제 후 모든 원소를 앞으로 이동시키기 때문에 시간 복잡도가 O(n)입니다.
# 마무리
- Python3를 위해 만들어진 문제는 아닌 것 같다. [tony repo 답지 코드](https://github.com/chjung99/baekjoon/blob/main/solution/graph_traversal/1325/main.cpp)
  를 봐도 c++로 단순한 dfs구현일 뿐 추가적인 알고리즘은 없다.

- Pypi3가 아닌 Python3로 구현한 풀이를 보면 dfs외 추가적인 로직이 필요하다, 이해하진 못했고 복잡해보여서 포기했다.
   
# 시간초과 풀이

```python
n, m = map(int, input().split())
graph = {i:[] for i in range(1,n+1)}
for i in range(m):
    e, s = map(int, input().split())
    graph[s].append(e)

def bfs(cur):
    visit = [0 for i in range(n+1)]
    visit[cur] = 1
    queue = [cur]
    cnt = 1
    while queue:
        cur = queue.pop(0) # 여기서 맨 앞 원소 제거 시 원소 개수만큼 시간 낭비 발생
        for nxt in graph[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                queue.append(nxt)
                cnt += 1
    return cnt

ans = []
for i in range(1,n+1):
    ans.append(bfs(i))

max_v = max(ans)

for i in range(n):
    if ans[i] == max_v:
        print(i+1, end=" ")
```
