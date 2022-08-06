from collections import deque


def topology_sort():
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])
            if indegree[i] == 0:
                q.append(i)

    print(dp[w])


T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    time = [0]
    time.extend(list(map(int, input().split())))
    dp = [0] * (n+1)

    for i in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(input())

    topology_sort()
