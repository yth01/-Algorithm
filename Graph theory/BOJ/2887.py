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
planets = []
for idx in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z, idx))
parent = [i for i in range(n+1)]

edges = []
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(n-1):
        cost = abs(planets[j][i]-planets[j+1][i])
        edges.append((cost, planets[j][3], planets[j+1][3]))
edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
