from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((j, i))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((nx, ny))

bfs()

result = 0
flag = False
for i in graph:
    for j in i:
        if j == 0:
            flag = True
            break
        result = max(result, j)

if flag == True:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result-1)
