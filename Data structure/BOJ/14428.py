import sys

INF = sys.maxsize

def input():
    return sys.stdin.readline()[:-1]


def getMinList(a, b):
    # Include index check
    if a[0] > b[0]:
        return b
    else:
        return a


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = getMinList(init(start, mid, node*2), init(mid+1, end, node*2+1))
        return tree[node]


def getMinValue(start, end, node, left, right):
    if left > end or right < start:
        return [INF, INF]
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return getMinList(getMinValue(start, mid, node*2, left, right), getMinValue(mid+1, end, node*2+1, left, right))


def update(start, end, node, index, diff):
    if start > index or end < index:
        return
    if start == end:
        tree[node] = diff
        return
    mid = (start + end) // 2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)
    tree[node] = getMinList(tree[node*2], tree[node*2+1])


n = int(input())
temp = list(map(int, input().split()))
data = [[0, 0] for _ in range(n)]
for i in range(n):
    data[i] = [temp[i], i+1]
tree = [[0, 0]] * (n*4)
init(0, n-1, 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 2:
        print(getMinValue(0, n-1, 1, b-1, c-1)[1])
    elif a == 1:
        data[b-1][0] = c
        update(0, n-1, 1, b-1, data[b-1])
