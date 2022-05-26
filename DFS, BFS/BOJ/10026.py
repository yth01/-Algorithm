from collections import deque
import sys

def input():
    return sys.stdin.readline()[:-1]

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny]:
                if graph[nx][ny] == graph[x][y]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        if graph[x][y] == 'G':
            graph[x][y] = 'R'

three_cnt = 0
two_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            three_cnt += 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            two_cnt += 1

print(three_cnt, two_cnt)
