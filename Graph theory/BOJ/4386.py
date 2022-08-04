from math import sqrt


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
stars = []
for _ in range(n):
    stars.append(list(map(float, input().split())))
parent = [i for i in range(n+1)]

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        cost = sqrt(pow(stars[i][0] - stars[j][0], 2) + pow(stars[i][1] - stars[j][1], 2))
        edges.append((cost, i, j))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(round(result, 2))
