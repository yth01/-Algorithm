DIV = 1000000007

def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node*2) * init(mid+1, end, node*2+1) % DIV
        return tree[node]
        

def prefixMul(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return prefixMul(start, mid, node*2, left, right) * prefixMul(mid+1, end, node*2+1, left, right) % DIV


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = diff
        return
    else:
        mid = (start + end) // 2
        update(start, mid, node*2, index, diff)
        update(mid+1, end, node*2+1, index, diff)
        tree[node] = tree[node*2] * tree[node*2+1] % DIV


n, m, k = map(int, input().split())
tree = [0] * (n*4)
data = []
for _ in range(n):
    data.append(int(input()))

init(0, n-1, 1)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)
    elif a == 2:
        print(prefixMul(0, n-1, 1, b-1, c-1))
