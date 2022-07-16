import sys

INF = int(1e9)


def input():
    return sys.stdin.readline()[:-1]


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
distance = [INF] * (n+1)


def bf(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            now_node = graph[j][0]
            next_node = graph[j][1]
            cost = graph[j][2]
            if distance[now_node] != INF and distance[next_node] > distance[now_node] + cost:
                distance[next_node] = distance[now_node] + cost
                if i == n - 1:
                    return True
    return False


negative_cycle = bf(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])
