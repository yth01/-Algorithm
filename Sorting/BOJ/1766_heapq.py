from heapq import heappush, heappop

def topology_sort():
    heap = []

    for i in range(1, n+1):
        if indegree[i] == 0:
            heappush(heap, i)

    while heap:
        now = heappop(heap)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heappush(heap, i)

    print(*result)


n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
result = []

topology_sort()
