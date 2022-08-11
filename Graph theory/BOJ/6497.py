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


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = []
    for _ in range(n):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))
    edges.sort()
    parent = [i for i in range(m+1)]

    result = 0
    total = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
        total += cost
    print(total-result)
