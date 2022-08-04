from collections import deque


def bfs():
    while q:
        x, log = q.popleft()
        if x == n:
            print(len(log)-1)
            print(*log[::-1])
            return
        for nx in (x*3, x*2, x+1):
            if nx <= n and not visited[nx]:
                visited[nx] = True
                q.append((nx, log+[nx]))


n = int(input())
q = deque()
q.append((1, [1]))
visited = [False] * (n+1)
bfs()
