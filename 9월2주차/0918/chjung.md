# 요약
- 시간 제한 1초, 3 ≤ N, M ≤ 100 이므로 O(NM) 탐색이어도 충분하다고 판단함, 따라서 **BFS알고리즘**으로 탐색함.
- "그람"만 없으면 일반적인 BFS 탐색문제이고, "그람"조건을 통해 벽부수기 가능한 조건이 추가됨.
- BFS 알고리즘과 dist 배열을 통해 최단거리 문제를 풀 수 있다.
# 설명
- 크게 두가지 경우의 수로 분리하였음
- 첫째, 용사에서 공주로 바로가는 경우
- 둘째, 용사에서 "그람"을 얻고, "그람"에서 공주로 가는 경우
  ```python
  if sword != (-1, -1):
    d_sword = n - 1 - sword[0] + m - 1 - sword[1]
    # print(d_sword)
    if dist[n-1][m-1] > dist[sword[0]][sword[1]] + d_sword:
        ans = dist[sword[0]][sword[1]] + d_sword
    else:
        ans = dist[n-1][m-1]
  else:
      ans = dist[n - 1][m - 1]
  ```
- 용사에서 공주까지의 거리를 구하는 방법은 bfs(0,0)를 한번 돌려서 (0,0)부터 모든 곳까지의 거리를 구하였음
- 이 과정에서 용사에서 "그람"까지의 거리 또한 구할 수 있음
- 마지막으로 "그람"에서 공주까지의 거리는 벽을 부술 수 있으므로 단순 [맨해튼 거리](https://ko.wikipedia.org/wiki/%EB%A7%A8%ED%95%B4%ED%8A%BC_%EA%B1%B0%EB%A6%AC)로 구했음
- 거리가 상대적으로 크냐 작냐를 기준으로 로직을 구현했기 때문에 dist 배열을 float("inf")로 초기화 하였음
  
  
# 마무리
- 이 문제 같은 경우 용사, 공주의 자리는 고정되어 있어서 로직 구현이 간편했음
- BFS에서 다음 노드로 방문할 때 dist배열을 업데이트해주는 방식으로 최단 거리를 구했음
- "그람"의 위치를 구하기 위해서 함수 외부에서 정의된 sword변수를 함수내에서 수정하기 위해 global sword로 선언해주었음
- deque를 사용하는 방법은
  1. import 하기 , from collections import deque
  2. 선언하기, queue = deque()
  3. 맨뒤에 삽입하기, queue.append(cur)
  4. 맨앞 가져오고 삭제하기, cur = queue.popleft()
```python
  def bfs(cur):# cur = (cur_x,cur_y)
    global sword
    queue = deque()
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[cur[0]][cur[1]] = 1

    queue.append(cur)
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nxt = cur[0]+dx[i], cur[1]+dy[i]
            if nxt[0] < 0 or nxt[0] >= n or nxt[1] < 0 or nxt[1] >= m:
                continue
            if visited[nxt[0]][nxt[1]] == 0 and matrix[nxt[0]][nxt[1]] != 1:
                if matrix[nxt[0]][nxt[1]] == 2:
                    sword = (nxt[0], nxt[1])
                visited[nxt[0]][nxt[1]] = 1
                queue.append(nxt)
                dist[nxt[0]][nxt[1]] = dist[cur[0]][cur[1]] + 1
```
