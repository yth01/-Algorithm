def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    else:
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
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node*2, index, diff)
        update(mid+1, end, node*2+1, index, diff)


n, m, k = map(int, input().split())
tree = [0] * (n*4)
data = []
for _ in range(n):
    data.append(int(input()))

init(0, n-1, 1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - data[b]
        data[b] = c
        update(0, n-1, 1, b, diff)
    elif a == 2:
        print(prefixSum(0, n-1, 1, b-1, c-1))
