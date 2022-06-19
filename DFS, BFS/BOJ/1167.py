from collections import deque

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(1, v+1):
    data = list(map(int, input().split()))
    a = data[0]
    data.pop()
    data = data[1:]
    while data:
        distance = data.pop()
        b = data.pop()
        graph[a].append((b, distance))


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
    visited = [False for _ in range(v+1)]
    queue = deque()
    queue.append((check, 0))
    visited[check] = True
    bfs(queue)
print(result)
