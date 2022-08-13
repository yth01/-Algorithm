import sys

INF = int(1e9)

def input():
    return sys.stdin.readline()[:-1]


def init(start, end, node):
    if start == end:
        tree[node] = [data[start], start]
        return tree[node]
    else:
        mid = (start + end) // 2
        init(start, mid, node*2)
        init(mid+1, end, node*2+1)
        
        min_idx = node*2
        if tree[node*2][0] > tree[node*2+1][0]:
            min_idx = node*2+1
        tree[node] = [tree[min_idx][0], tree[min_idx][1]]


def update(start, end, node, index, diff):
    if start > index or end < index:
        return
    if start == end:
        tree[node] = [diff, start]
        return

    mid = (start + end) // 2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

    min_idx = node*2
    if tree[node*2][0] > tree[node*2+1][0]:
        min_idx = node*2+1
    tree[node] = [tree[min_idx][0], tree[min_idx][1]]


n = int(input())
data = list(map(int, input().split()))
m = int(input())
tree = [[0, 0]] * (n*4)
init(0, n-1, 1)
for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 2:
        print(tree[1][1] + 1)
    elif cmd[0] == 1:
        a, b = cmd[1], cmd[2]
        data[a-1] = b
        update(0, n-1, 1, a-1, b)
