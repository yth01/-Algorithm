import sys

INF = int(1e9)


def input():
    return sys.stdin.readline()[:-1]


tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
    distance = [INF] * (n+1)

    def bf(start):
        distance[start] = 0
        for i in range(n):
            for j in range(m*2+w):
                now_node = graph[j][0]
                next_node = graph[j][1]
                cost = graph[j][2]
                if distance[next_node] > distance[now_node] + cost:
                    distance[next_node] = distance[now_node] + cost
                    if i == n - 1:
                        return True
        return False
    
    negative_cycle = bf(1)

    print("YES" if negative_cycle else "NO")
