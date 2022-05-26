from collections import deque

n, m, h = map(int, input().split())
graph = []
for i in range(h):
    graph.append([])
    for _ in range(m):
        graph[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for i in range(h):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 1:
                queue.append((k, j, i))

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nx, ny, nz))

bfs()

result = 0
flag = False
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                flag = True
                break
            result = max(result, k)

if flag == True:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)
