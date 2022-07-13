import sys
import heapq

INF = int(1e9)


def input():
	return sys.stdin.readline()[:-1]


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

start, goal = map(int, input().split())
history= [[] for _ in range(n+1)]


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
				history[loc].clear()
				history[loc].extend(history[now])
				history[loc].append(loc)

				distance[loc] = cost
				heapq.heappush(q, (cost, loc))


dijkstra(start)
# Insert start node
for i in history:
    i.insert(0, start)

print(distance[goal])
print(len(history[goal]))
for i in history[goal]:
	print(i, end=' ')

