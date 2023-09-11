from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n+1)}
ans = []
max_v = -1
for i in range(m):
    e, s = map(int, input().split())
    graph[s].append(e)


def bfs(cur):
    visit = [0 for i in range(n+1)]
    visit[cur] = 1
    queue = deque([cur])
    cnt = 1
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                queue.append(nxt)
                cnt += 1
    return cnt


for i in range(1, n+1):
    ret = bfs(i)
    if max_v < ret:
        max_v = ret
    ans.append(ret)

for i in range(n):
    if ans[i] == max_v:
        print(i+1, end=" ")
