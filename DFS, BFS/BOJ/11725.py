from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n+1)]


def bfs(q):
    while q:
        parent_node = q.popleft()
        for child_node in graph[parent_node]:
            if not visited[child_node]:
                if result[child_node] == 0:
                    result[child_node] = parent_node
                visited[child_node] = True
                q.append(child_node)


result = [0 for _ in range(n+1)]
queue = deque([1])
visited[1] = True
bfs(queue)
for i in result[2:]:
    print(i)
