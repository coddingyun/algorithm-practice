from collections import deque

n, m, t = map(int, input().split())
matrix = []
dist = [[float("inf") for i in range(m)] for j in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dist[0][0] = 0
sword = (-1, -1)
for i in range(n):
    matrix.append(list(map(int, input().split())))


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


bfs((0, 0))

# 1. if d용사-공주 > d용사-그람-공주 : 용사 -> 그람 -> 공주
# 2. else : 용사 -> 공주
ans = 0
if sword != (-1, -1):
    d_sword = n - 1 - sword[0] + m - 1 - sword[1]
    # print(d_sword)
    if dist[n-1][m-1] > dist[sword[0]][sword[1]] + d_sword:
        ans = dist[sword[0]][sword[1]] + d_sword
    else:
        ans = dist[n-1][m-1]
else:
    ans = dist[n - 1][m - 1]

if ans <= t:
    print(ans)
else:
    print("Fail")

