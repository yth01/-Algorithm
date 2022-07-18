def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for a in range(n):
    data = list(map(int, input().split()))
    for b in range(n):
        if data[b]:
            union_find(parent, a+1, b+1)

plan = list(map(int, input().split()))
root = find_parent(parent, plan[0])
flag = True
for i in plan[1:]:
    if root == find_parent(parent, i):
        root = find_parent(parent, i)
    else:
        flag = False
        break
print("YES" if flag else "NO")
