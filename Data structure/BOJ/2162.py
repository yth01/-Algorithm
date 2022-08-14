from collections import Counter


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


def ccw(a, b, c):
    c = (a[0]*b[1]+b[0]*c[1]+c[0]*a[1])-(b[0]*a[1]+a[0]*c[1]+c[0]*b[1])
    if c > 0:
        return 1
    elif c < 0:
        return -1
    else:
        return 0


def check(A, B, C, D):
    if ccw(A,B,C)*ccw(A,B,D) <= 0 and ccw(C,D,A)*ccw(C,D,B) <= 0:
        if ccw(A,B,C)*ccw(A,B,D) == 0 and ccw(C,D,A)*ccw(C,D,B) == 0:
            if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0


n = int(input())
lines = [[]]
for _ in range(n):
    lines.append(list(map(int, input().split())))
parent = [i for i in range(n+1)]

for i in range(1, n):
    for j in range(i+1, n+1):
        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        A = [x1, y1]
        B = [x2, y2]
        C = [x3, y3]
        D = [x4, y4]
        if check(A, B, C, D):
            union_parent(parent, i, j)

for i in range(1, n+1):
    parent[i] = find_parent(parent, i)
result = Counter(parent[1:])
print(len(result))
print(max(result.values()))
