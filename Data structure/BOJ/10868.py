import sys

INF = int(1e9)

def input():
    return sys.stdin.readline()[:-1]


def initMin(start, end, node):
    if start == end:
        tree_min[node] = data[start]
        return tree_min[node]
    else:
        mid = (start + end) // 2
        tree_min[node] = min(initMin(start, mid, node*2), initMin(mid+1, end, node*2+1))
        return tree_min[node]


def getMin(start, end, node, left, right):
    if left > end or right < start:
        return INF
    if left <= start and right >= end:
        return tree_min[node]
    mid = (start + end) // 2
    return min(getMin(start, mid, node*2, left, right), getMin(mid+1, end, node*2+1, left, right))


n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

tree_min = [0] * (n*4)
initMin(0, n-1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(getMin(0, n-1, 1, a-1, b-1))
