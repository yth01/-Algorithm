from collections import deque
INF = int(1e9)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 2
now_x, now_y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[now_x][now_y] = 0

def bfs():
    visited = [[-1] * n for _ in range(n)]
    visited[now_x][now_y] = 0
    queue = deque([(now_x, now_y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == -1 and graph[nx][ny] <= size:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return visited

def find(visited):
    x, y = 0, 0
    min_value = INF
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and 1 <= graph[i][j] < size:
                if visited[i][j] < min_value:
                    x, y = i, j
                    min_value = visited[x][y]
    if min_value == INF:
        return None
    else:
        return x, y, min_value

result = 0
ate = 0
while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        graph[now_x][now_y] = 0
        ate += 1
        if size == ate:
            size += 1
            ate = 0
