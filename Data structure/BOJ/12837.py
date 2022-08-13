import sys

def input():
    return sys.stdin.readline()[:-1]


def prefixSum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return prefixSum(start, mid, node*2, left, right) + prefixSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node*2, index, diff)
        update(mid+1, end, node*2+1, index, diff)


n, q = map(int, input().split())
tree = [0] * (n*4)
data = [0] * n
for _ in range(q):
    cmd, p, q = map(int, input().split())
    if cmd == 1:
        data[p-1] -= q
        update(0, n-1, 1, p-1, q)
    elif cmd == 2:
        print(prefixSum(0, n-1, 1, p-1, q-1))
