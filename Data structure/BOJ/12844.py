import sys

def input():
    return sys.stdin.readline()[:-1]


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) ^ init(mid+1, end, node*2+1)
    return tree[node]


def prefixSum(start, end, node, left, right):
    propagate(start, end, node)
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return prefixSum(start, mid, node*2, left, right) ^ prefixSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, left, right, diff):
    propagate(start, end, node)
    if left > end or right < start:
        return
    
    if left <= start and end <= right:
        if ((end-start+1)%2) == 1:
            tree[node] ^= diff
        if start != end:
            lazy[node*2] ^= diff
            lazy[node*2+1] ^= diff
        return

    mid = (start + end) // 2
    update(start, mid, node*2, left, right, diff)
    update(mid+1, end, node*2+1, left, right, diff)
    tree[node] = tree[node*2] ^ tree[node*2+1]


def propagate(start, end, node):
    if lazy[node] != 0:
        if ((end-start+1)%2) == 1:
            tree[node] ^= lazy[node]
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0


n = int(input())
data = list(map(int, input().split()))
tree = [0] * (n*4)
lazy = [0] * (n*4)
init(0, n-1, 1)
m = int(input())
for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 2:
        i, j = cmd[1], cmd[2]
        print(prefixSum(0, n-1, 1, i, j))
    elif cmd[0] == 1:
        i, j, k = cmd[1], cmd[2], cmd[3]
        update(0, n-1, 1, i, j, k)
