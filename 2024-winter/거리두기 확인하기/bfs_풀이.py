from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(graph, x, y):
    q = deque([])
    visited = [[False]*5 for _ in range(5)]
    distance = [[0]*5 for _ in range(5)]
    
    q.append((x, y))
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == False:
                if graph[nx][ny] == 'X':
                    visited[nx][ny] = True
                    continue
                elif graph[nx][ny] == 'P':
                    if distance[cx][cy] <=1:
                        return False
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[cx][cy]+1
    return True

def solution(places):
    answer = []
    for place in places:
        flag = True
        for i in range(5):
            if flag == False:
                break
            for j in range(5):
                if place[i][j] == 'P':
                    if check(place, i, j) == False:
                        print(i, j)
                        flag = False
                        break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
             
    return answer
