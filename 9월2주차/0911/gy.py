import sys
input = sys.stdin.readline
from collections import deque

def bfs(a):
  visited = [False]*(n+1)
  num = 0
  q = deque([a])
  visited[a] = True
  while q:
    item = q.popleft()
    for a in graph[item]:
      if visited[a] == False:
        visited[a] = True
        q.append(a)
        num += 1
  return num

n, m = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]

start_com = set()

for _ in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)
  start_com.add(b)

total = -1
answer = []

for item in start_com:
  result = bfs(item)
  if total < result:
    answer = [item]
    total = result
  elif total == result:
    answer.append(item)

answer = sorted(answer)
for i in answer:
  print(i, end=' ')
    
  
