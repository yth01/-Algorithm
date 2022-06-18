from collections import deque
import copy

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
# Find 2 value
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            queue.append((i, j))                


def AddWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                AddWall(cnt + 1)
                graph[i][j] = 0
 

def bfs():
    q = copy.deepcopy(queue)
    temp_graph = copy.deepcopy(graph)
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < m and temp_graph[nr][nc] == 0:
                temp_graph[nr][nc] = 2
                q.append((nr, nc))

    # Update 0 count
    global result
    temp = 0
    for i in range(n):
        temp += temp_graph[i].count(0)
    result = max(result, temp)

         

result = 0
AddWall(0)
print(result)
