from collections import deque

n, m = map(int, input().split())
up = [0 for _ in range(101)]
down = [0 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    up[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    down[a] = b

visited = [0 for _ in range(101)]

def bfs():
    q = deque([1])
    while q:
        x = q.popleft()
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            if up[nx] != 0:
                nx = up[nx]
            if down[nx] != 0:
                nx = down[nx]
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs()
print(visited[100])
