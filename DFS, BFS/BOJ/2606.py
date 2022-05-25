def dfs(graph, v, visited):
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

com = int(input())
n = int(input())
graph = [[] for _ in range(com+1)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (com + 1)

result = []
dfs(graph, 1, visited)
print(len(result)-1)
