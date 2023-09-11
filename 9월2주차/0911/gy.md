## 찬호님 풀이와 다른점
1. 마지막 bfs를 도는 대상을 제한하였음. => input을 받을 때 B만 따로 set에 저장해두어 B만 bfs 대상이 되도록
2. 마지막 가장 큰 수를 가지는 컴퓨터 넘버를 구하는 경우, bfs 값이 더 크면 answer을 item만 담도록 초기화하고 값이 같으면 answer에 추가.

## 삽질 과정
1. dfs
```
def dfs(a):
  global num
  visited.add(a)
  for item in graph[a]:
    if item not in visited:
      num += 1
      dfs(item)
```
** 주의: parameter는 global로 설정 할 수 없음. 함수내의 값이 밖에서도 적용되려면, 아예 파라미터에서 제거해야함.
** dfs로는 풀 수 있는 방법이 없다.

2. bfs
```
def bfs(a):
  num = 0
  q = deque([a])
  visited[a] = True
  while q:
    item = q.popleft()
    for a in graph[item]:
      if a not in visited:
        visited.add(a)
        q.append(a)
        num += 1
  return num
```
이때 set이면, if a not in visited에서 set을 한번 전체 돌아야 한다. 따라서 리스트 인덱스로 바로 접근하여 시간을 줄여야 시간초과가 나지 않는다.

## 비고
Pypy3만 된다. 파이썬에게는 썩 좋은 문제는 아닌듯
