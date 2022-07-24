n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
count = 0


def dfs(r, c, shape):
    global count
    if r == n-1 and c == n-1:
        count += 1
        return
    if 0 <= r+1 < n and 0 <= c+1 < n:
        if graph[r+1][c+1] == 0 and graph[r+1][c] == 0 and graph[r][c+1] == 0:
            dfs(r+1, c+1, 2)
    if r+1 < n:
        if (shape == 1 or shape == 2) and graph[r+1][c] == 0:
            dfs(r+1, c, 1)
    if c+1 < n:
        if (shape == 0 or shape == 2) and graph[r][c+1] == 0:
            dfs(r, c+1, 0)
       
       
dfs(0, 1, 0)
print(count)
