import sys
import heapq

INF = int(1e9)


def input():
	return sys.stdin.readline()[:-1]


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
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


dijkstra(x)
main_distance = distance
result = 0
for i in range(1, n+1):
	if i == x:
		continue
	distance = [INF] * (n+1)
	dijkstra(i)
	result = max(distance[x] + main_distance[i], result)

print(result)
