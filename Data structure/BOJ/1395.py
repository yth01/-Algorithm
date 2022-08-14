def prefixSum(start, end, node, left, right):
    propagate(start, end, node)
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return prefixSum(start, mid, node*2, left, right) + prefixSum(mid+1, end, node*2+1, left, right)


def update(start, end, node, left, right):
    propagate(start, end, node)
    if left > end or right < start:
        return
    
    if left <= start and end <= right:
        tree[node] = (end-start+1) - tree[node]
        if start != end:
            lazy[node*2] = not lazy[node*2]
            lazy[node*2+1] = not lazy[node*2+1]
        return

    mid = (start + end) // 2
    update(start, mid, node*2, left, right)
    update(mid+1, end, node*2+1, left, right)
    tree[node] = tree[node*2] + tree[node*2+1]


def propagate(start, end, node):
    if lazy[node] != 0:
        tree[node] = (end-start+1) - tree[node]
        if start != end:
            lazy[node*2] = not lazy[node*2]
            lazy[node*2+1] = not lazy[node*2+1]
        lazy[node] = 0


n, m = map(int, input().split())
tree = [0] * (n*4)
lazy = [0] * (n*4)
for _ in range(m):
    cmd, s, t = map(int, input().split())
    if cmd == 1:
        print(prefixSum(0, n-1, 1, s-1, t-1))
    elif cmd == 0:
        update(0, n-1, 1, s-1, t-1)
