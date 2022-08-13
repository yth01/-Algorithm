import sys

INF = int(1e9)

def input():
    return sys.stdin.readline()[:-1]


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(start, mid, node*2), init(mid+1, end, node*2+1))
        return tree[node]


def prefixSum(start, end, node, left, right):
    if left > end or right < start:
        return INF
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return min(prefixSum(start, mid, node*2, left, right), prefixSum(mid+1, end, node*2+1, left, right))


def update(start, end, node, index, diff):
    if start > index or end < index:
        return INF
    if start == end:
        tree[node] = diff
        return tree[node]
    else:
        mid = (start + end) // 2
        update(start, mid, node*2, index, diff)
        update(mid+1, end, node*2+1, index, diff)
        tree[node] = min(tree[node*2], tree[node*2+1])


n = int(input())
data = list(map(int, input().split()))
m = int(input())
tree = [0] * (n*4)
init(0, n-1, 1)
for _ in range(m):
    cmd, i, k = map(int, input().split())
    if cmd == 2:
        print(prefixSum(0, n-1, 1, i-1, k-1))
    elif cmd == 1:
        data[i-1] = k
        update(0, n-1, 1, i-1, k)
