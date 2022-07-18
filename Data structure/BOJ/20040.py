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


n, m = map(int, input().split())
parent = [0] * n

for i in range(n):
    parent[i] = i

history = []
result = 0
flag = False
for _ in range(m):
    a, b = map(int, input().split())
    result += 1
    if find_parent(parent, a) == find_parent(parent, b):
        flag = True
        break
    else:
        union_parent(parent, a, b)

if flag:
    print(result)
else:
    print(0)
