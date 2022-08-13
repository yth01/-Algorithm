def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2+1)
    return tree[node]

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

n, q = map(int, input().split())
data = list(map(int, input().split()))
tree = [0] * (n*4)
init(0, n-1, 1)
for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x < y:
        print(prefixSum(0, n-1, 1, x-1, y-1))
    else:
        print(prefixSum(0, n-1, 1, y-1, x-1))
    diff = b - data[a-1]
    data[a-1] = b
    update(0, n-1, 1, a-1, diff)
