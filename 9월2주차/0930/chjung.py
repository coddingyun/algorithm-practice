from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]
dist = [0 for _ in range(n+1)]
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
s, e = map(int, input().split())
for i in range(n):
    graph[i].sort()

queue = deque([s])
visit[s] = 1

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if visit[nxt] == 0:
            queue.append(nxt)
            visit[nxt] = 1
            dist[nxt] = dist[cur] + 1


visit = [0 for _ in range(n+1)]
queue = deque([e])
visit[e] = 1
while queue:
    cur = queue.popleft()
    if cur == s:
        continue
    min_dist = 100000
    min_node = 0
    for nxt in graph[cur]:
        if min_dist > dist[nxt]:
            min_dist = dist[nxt]
            min_node = nxt
    visit[min_node] = 1
    queue.append(min_node)

answer += dist[e]

visit[e] = 0
visit[s] = 0

dist = [0 for _ in range(n+1)]
queue = deque([e])
visit[e] = 1

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if visit[nxt] == 0:
            queue.append(nxt)
            visit[nxt] = 1
            dist[nxt] = dist[cur] + 1

answer += dist[s]

print(answer)
