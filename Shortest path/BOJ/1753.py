import heapq
import sys


def input():
    return sys.stdin.readline()[:-1]


INF = int(1e9)

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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


dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
