from collections import deque

w, h = map(int, input().split())
matrix = []
graph = [[[0 for i in range(6)] for j in range(w)] for k in range(h)]
visit = [[0 for i in range(w)] for j in range(h)]
ans = 0

dx_even = [1, 1, 0, -1, 0, 1]
dy_even = [0, 1, 1, 0, -1, -1]

dx_odd = [1, 0, -1, -1, -1, 0]
dy_odd = [0, 1, 1, 0, -1, -1]

for i in range(h):
    line = list(map(int, input().split()))
    matrix.append(line)
  
for y in range(h):
    for x in range(w):

        if y % 2 == 0:
            dx = dx_even
            dy = dy_even
        else:
            dx = dx_odd
            dy = dy_odd
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if matrix[y][x] == 1 and matrix[ny][nx] == 1:
                graph[y][x][i] = 1
            elif matrix[y][x] == 0 and matrix[ny][nx] == 0:
                graph[y][x][i] = 2


def bfs(cy, cx, tar):
    global visit
    is_inside = True
    cnt = 0
    visit[cy][cx] = 1
    # print(cx + 1, cy + 1)
    queue = deque([(cy, cx)])

    while queue:
        cur = queue.popleft()  # (y,x)
        cnt += graph[cur[0]][cur[1]].count(0)
        if cur[0] % 2 == 0:
            ddx = dx_even
            ddy = dy_even
        else:
            ddx = dx_odd
            ddy = dy_odd
        for i in range(6):
            nnx = cur[1] + ddx[i]
            nny = cur[0] + ddy[i]
            if nnx < 0 or nnx >= w or nny < 0 or nny >= h:
                if tar == 0:
                    is_inside = False
                continue
            if graph[cur[0]][cur[1]][i] == 2-tar and visit[nny][nnx] == 0 and matrix[nny][nnx] == tar:
                queue.append((nny, nnx))
                visit[nny][nnx] = 1
                # print(nnx+1,nny+1)
    if is_inside == False:
        cnt = 0
    return cnt



for y in range(h):
    for x in range(w):

        if visit[y][x] == 0 and matrix[y][x] == 1:
            ans += bfs(y, x, 1)
        elif visit[y][x] == 0 and matrix[y][x] == 0:
            ans -= bfs(y, x, 0)

print(ans)
