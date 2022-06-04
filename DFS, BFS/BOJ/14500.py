def dfs(x, y, total, cnt):
    global result
    if cnt == 4:
        result = max(result, total)
        return True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = True
                dfs(x, y, total + data[nx][ny], cnt+1)
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, total + data[nx][ny], cnt+1)
            visited[nx][ny] = False

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, data[i][j], 1)
        visited[i][j] = False
print(result) 
