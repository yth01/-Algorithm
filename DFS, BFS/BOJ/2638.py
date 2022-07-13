import sys
from collections import deque

INF = int(1e9)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def input():
    return sys.stdin.readline()[:-1]


def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and data[nr][nc] != INF:
                if not data[nr][nc]:
                    data[nr][nc] = INF
                    q.append((nr, nc))
                elif data[nr][nc] <= 2:
                    data[nr][nc] += 1  


def postprocessing():
    for r in range(n):
        for c in range(m):
            if data[r][c] >= 3:
                data[r][c] = 0
            elif data[r][c] == 0:
                continue
            else:
                data[r][c] = 1


def search_all():
    for r in range(n):
        for c in range(m):
            if data[r][c] == 1:
                return True
    return False
            

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

time = 0
while True:
    if search_all():
        bfs(0, 0)
        postprocessing()
        time += 1
    else:
        print(time)
        break
