from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    def dfs(x, y):
        if x < 0 or y < 0 or x >= m or y >= n:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        return False

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                result += 1
    print(result)
