from collections import deque

n, k = map(int, input().split())

visited = [-1] * 100001
result = 0


def bfs(q):
    global result
    while q:
        x, cnt = q.popleft()
        if x == k:
            result += 1
            continue
        for nx in (x*2, x+1, x-1):
            if 0 <= nx < 100001 and (visited[nx] == -1 or visited[nx] == visited[x] + 1):
                visited[nx] = visited[x] + 1
                q.append((nx, visited[nx]))


queue = deque()
queue.append((n, 0))
visited[n] = 0
bfs(queue)

print(visited[k])
print(result)
