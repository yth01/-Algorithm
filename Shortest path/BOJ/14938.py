import sys
from heapq import heappush, heappop

INF = int(1e9)


def input():
    return sys.stdin.readline()[:-1]


n, m, r = map(int, input().split())

nodes = [0]
nodes.extend(list(map(int, input().split())))

graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for loc, pre_dist in graph[now]:
            cost = dist + pre_dist
            if cost < distance[loc]:
                distance[loc] = cost
                heappush(q, (cost, loc))


result = 0
for i in range(1, n+1):
    distance = [INF] * (n+1)
    dijkstra(i)

    items = 0
    distance = list(map(lambda x: x if x <= m else INF, distance))
    for i in range(1, n+1):
        if distance[i] < INF:
            items += nodes[i]
    result = max(result, items) 

print(result)
