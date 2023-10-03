from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

s, e = map(int, input().split())

for i in range(n+1):
  graph[i].sort()

visited = [0]*(n+1)
queue = deque([[s, 0, [s]]])
visited[s] = True

answer = 0

while queue:
  nx, ncount, nq = queue.popleft()
  if nx == e:
    for i in range(len(visited)):
      visited[i] = 0
    for i in range(1, len(nq)):
      visited[nq[i]] = 2
    answer += ncount
    break
  for item in graph[nx]:
    if visited[item] == 0:
      visited[item] = 1
      queue.append([item, ncount+1, nq+[item]])


reverseQueue = deque([[e, 0, [e]]])

while reverseQueue:
  nx, ncount, nq = reverseQueue.popleft()
  if nx == s:
    answer += ncount
  for item in graph[nx]:
    if visited[item] == 0:
      visited[item] = 2
      reverseQueue.append([item, ncount+1, nq + [item]])

print(answer)
