from bisect import bisect_right


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


n, m, k = map(int, input().split())
number = sorted(list(map(int, input().split())))
cards = list(map(int, input().split()))
parent = [i for i in range(m+1)]
result = []

for card in cards:
    idx = bisect_right(number, card)
    idx = find_parent(parent, idx)
    result.append(number[idx])
    union_parent(parent, idx, idx+1)

for i in result:
    print(i)
