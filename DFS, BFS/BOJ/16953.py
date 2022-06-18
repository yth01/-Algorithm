from collections import deque

a, b = map(int, input().split())


def bfs(q):
    while q:
        n, cnt = q.popleft()
        if n == b:
            return cnt
        for nx in (int(str(n) + '1'), n * 2):
            if nx <= b:
                q.append((nx, cnt+1))
    return -1 


queue = deque()
queue.append((a, 1))
print(bfs(queue))
