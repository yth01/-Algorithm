from collections import deque

MAX = 100000

n, k = map(int, input().split())
visited = [-1] * (MAX+1)


def bfs(start):
    q = deque([start])
    visited[start] = 0
    while q:
        x = q.popleft()
        if x == k:
            return visited[x]
        for nx in (x*2, x+1, x-1):
            if 0 <= nx <= MAX and visited[nx] == -1:
                if nx == x*2:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
        

print(bfs(n))
