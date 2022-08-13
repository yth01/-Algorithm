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
    if start > index or end < index:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node*2, index, diff)
        update(mid+1, end, node*2+1, index, diff)


n, m = map(int, input().split())
data = [0] * n
tree = [0] * (n*4)
for _ in range(m):
    cmd, i, k = map(int, input().split())
    if cmd == 0:
        if i < k:
            print(prefixSum(0, n-1, 1, i-1, k-1))
        else:
            print(prefixSum(0, n-1, 1, k-1, i-1))
    elif cmd == 1:
        diff = k - data[i-1]
        data[i-1] = k
        update(0, n-1, 1, i-1, diff)
