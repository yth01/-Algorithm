import sys

INF = int(1e9)


def input():
    return sys.stdin.readline()[:-1]


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# find house, chiken location
house_location = []
chiken_location = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house_location.append((r, c))
        elif graph[r][c] == 2:
            chiken_location.append((r, c))
            graph[r][c] = 0
house_location.sort()
chiken_location.sort()

stack = []
result = INF


def sum_distance():
    total = 0
    for house_r, house_c in house_location:
        shortest_chiken = INF
        for chiken_r, chiken_c in stack:
            shortest_chiken = min(shortest_chiken, abs(house_r - chiken_r) + abs(house_c - chiken_c))
        total += shortest_chiken
    return total


def dfs(start):
    global result
    if len(stack) == m:
        for i in range(m):
            r, c = stack[i]
            graph[r][c] = 2
        result = min(result, sum_distance())
        return

    for i in range(start, len(chiken_location)):
        stack.append(chiken_location[i])
        dfs(i+1)
        delete_r, delete_c = stack.pop()
        graph[delete_r][delete_c] = 0
    return result


print(dfs(0))
