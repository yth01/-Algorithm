import heapq
import sys


def input():
    return sys.stdin.readline()[:-1]


INF = int(1e9)

start = 1
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for loc, pre_dist in graph[now]:
            cost = dist + pre_dist
            if cost < distance[loc]:
                distance[loc] = cost
                heapq.heappush(q, (cost, loc))


result_v1 = 0
result_v2 = 0

dijkstra(start)
result_v1 += distance[v1]
result_v2 += distance[v2]

distance = [INF] * (n+1)
dijkstra(v1)
result_v1 += distance[v2]
result_v2 += distance[n]

distance = [INF] * (n+1)
dijkstra(v2)
result_v1 += distance[n]
result_v2 += distance[v1]

result = min(result_v1, result_v2)
print(result if result < INF else '-1')
