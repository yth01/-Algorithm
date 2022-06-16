from collections import deque

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs(q):
    while q:
        r, c, flag = q.popleft()
        if r == n-1 and c == m-1:
            return visited[r][c][flag]
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < m:
                if flag == 0 and data[nr][nc] == 1:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    q.append((nr, nc, 1))
                if data[nr][nc] == 0 and visited[nr][nc][flag] == 0:
                    visited[nr][nc][flag] = visited[r][c][flag] + 1
                    q.append((nr, nc, flag))
    return -1


q = deque()
q.append((0, 0, 0))
visited[0][0][0] = 1
print(bfs(q))
