import sys
sys.setrecursionlimit(10**9)

dx = [1,0,0,-1]
dy = [0,-1,1,0]
value = ['d', 'l', 'r', 'u']

def findPath(n, m, x, y, r, c, k, result, curK):
    if curK == k and x == r and y == c:
        return result

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if abs(nx - r) + abs(ny - c) + curK + 1 > k: continue
        if 1 <= nx <= n and 1 <= ny <= m:
            return findPath(n, m, nx, ny, r, c, k, result+value[i], curK+1)
            break

def solution(n, m, x, y, r, c, k):
    if (abs(x-r)+abs(y-c)+k)%2==1 or abs(x-r)+abs(y-c) > k:
        return "impossible"
    answer = findPath(n, m, x, y, r, c, k, "", 0)
    return answer
