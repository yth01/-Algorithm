INF = int(1e9)

n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            graph[i+1][j+1] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(1 if graph[i][j] != INF else 0, end=' ')
    print()
