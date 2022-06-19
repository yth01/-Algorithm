from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, distance = map(int, input().split())
    graph[a].append((b, distance))
    graph[b].append((a, distance))


def bfs(q):
    global check
    global result
    while q:
        now_node, now_distance = q.popleft()
        if now_distance > result:
            check = now_node
            result = now_distance
        for node, distance in graph[now_node]:
            if not visited[node]:
                visited[node] = True
                q.append((node, now_distance + distance))


check = 1
result = 0
for _ in range(2):
    visited = [False for _ in range(n+1)]
    queue = deque()
    queue.append((check, 0))
    visited[check] = True
    bfs(queue)
print(result)
