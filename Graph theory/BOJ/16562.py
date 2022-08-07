def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if friends_fee[a] <= friends_fee[b]:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
friends_fee = [0] + list(map(int, input().split()))
parent = [i for i in range(n+1)]
for _ in range(m):
    v, w = map(int, input().split())
    union_parent(parent, v, w)

result = 0
visited = []
for i in list(set(parent[1:])):
    idx = find_parent(parent, i)
    if idx not in visited:
        visited.append(idx)
        result += friends_fee[idx]
print(result if result <= k else "Oh no")
