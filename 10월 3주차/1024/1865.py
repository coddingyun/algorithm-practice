import sys
input = sys.stdin.readline

tc = int(input())

INF = int(1e9)

for _ in range(tc):
  n, m, w = map(int, input().split())
  info = []
  dist = [INF]*(n+1)
  dist

  for _ in range(m):
    s, e, t = map(int, input().split())
    info.append((s, e, t))
    info.append((e, s, t))

  for _ in range(w):
    s, e, t = map(int, input().split())
    info.append((s, e, -t))

  flag = False
  dist[1] = 0
  for i in range(1, n+1):
    for j in range(len(info)):
      s, e, t = info[j]
      if dist[e] > dist[s] + t:
        dist[e] = dist[s] + t
        if i == n:
          flag = True
  if flag == False:
    print('NO')
  else:
    print('YES')
