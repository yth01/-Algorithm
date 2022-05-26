from collections import deque

def bfs(a, visited):
    queue = deque()
    queue.append((a, ""))
    while queue:
        a, cmd = queue.popleft()
        visited[a] = True
        if a == b:
            print(cmd)

        # command D
        num = (2*a) % 10000
        if not visited[num]:
            visited[num] = True
            queue.append((num, cmd + "D"))

        # command S
        num = a-1 if a != 0 else 9999
        if not visited[num]:
            visited[num] = True
            queue.append((num, cmd + "S"))

        # command L
        num = (a % 1000 * 10) + (a // 1000)
        if not visited[num]:
            visited[num] = True
            queue.append((num, cmd + "L"))

        # command R
        num = (a % 10 * 1000) + (a // 10)
        if not visited[num]:
            visited[num] = True
            queue.append((num, cmd + "R"))

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    visited = [False] * 10001
    bfs(a, visited)
