from collections import deque

matrix = []
blocks = deque([])
new_blocks = deque([])
visit = [[[0 for i in range(8)] for j in range(8)] for j in range(100)]

dx = [0, 1, 0, -1, 1, 1, -1, -1, 0]
dy = [1, 0, -1, 0, -1, 1, -1, 1, 0]

for i in range(8):
    line = list(input())
    for j in range(8):
        if line[j] == '#':
            blocks.append((i, j))
    matrix.append(line)

queue = deque([])
queue.append((0, 7, 0))  # t,x,y
visit[0][7][0] = 1
cnt = 0
while queue:
    cur = queue.popleft()
    if cnt < cur[0]:
        cnt = cur[0]
        while blocks:
            block = blocks.popleft()
            matrix[block[0]][block[1]] = '.'
            if block[0] + 1 <= 7:
                new_blocks.append((block[0] + 1, block[1]))

        while new_blocks:
            new_block = new_blocks.popleft()
            matrix[new_block[0]][new_block[1]] = '#'
            blocks.append(new_block)

    if matrix[cur[1]][cur[2]] == '#' or cnt >= 99:
        continue

    for i in range(9):
        nt = cur[0] + 1
        nx = cur[1] + dx[i]
        ny = cur[2] + dy[i]

        if nx < 0 or nx >= 8 or ny < 0 or ny >= 8 or nt >= 100:
            continue

        if visit[nt][nx][ny] == 0 and matrix[nx][ny] == '.':
            queue.append((nt, nx, ny))
            visit[nt][nx][ny] = 1

answer = 0
for i in range(100):
    if visit[i][0][7] == 1:
        answer = 1
        break
print(answer)
