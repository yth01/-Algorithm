import heapq

MAX = 100000
INF = int(1e9)

n, k = map(int, input().split())
visited = [INF] * (MAX+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    visited[start] = 0
    while q:
        time, x = heapq.heappop(q)
        if x == k:
            return time
        for nx in (x*2, x+1, x-1):
            if 0 <= nx <= MAX and time < visited[nx]:
                if nx == x*2:
                    visited[nx] = time
                    heapq.heappush(q, (time, nx))
                else:
                    visited[nx] = time + 1
                    heapq.heappush(q, (time + 1, nx))


print(dijkstra(n))
