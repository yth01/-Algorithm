def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i)
