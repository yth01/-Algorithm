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


g = int(input())
p = int(input())
planes = []
for _ in range(p):
    planes.append(int(input()))
parent = [i for i in range(g+1)]

cnt = 0
for plane in planes:
    p = find_parent(parent, plane)
    if p == 0:
        break
    cnt += 1
    union_parent(parent, p-1, p)
print(cnt)
