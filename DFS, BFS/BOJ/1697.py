from collections import deque

def bfs():
    queue = deque([n])
    while queue:
        v = queue.popleft()
        if v == k:
            print(visited[v])
            break
        for nx in (v-1, v+1, v*2):
            if 0 <= nx <= MAX and not visited[nx]:
                visited[nx] = visited[v] + 1
                queue.append(nx)

MAX = 100000
visited = [0] * (MAX + 1)
n, k = map(int, input().split())

bfs()
