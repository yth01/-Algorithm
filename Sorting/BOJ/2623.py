from collections import deque


def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    if len(result) == n:
        for i in result:
            print(i)
    else:
        print(0)


n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    turns = list(map(int, input().split()))
    team_num = turns[0]
    turns = turns[1:]
    for i in range(team_num-1):
        a = turns[i]
        b = turns[i+1]
        graph[a].append(b)
        indegree[b] += 1
result = []

topology_sort()
