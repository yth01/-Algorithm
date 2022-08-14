import sys

def input():
    return sys.stdin.readline()[:-1]


def checkEven(n):
    if n % 2 == 0:
        return 1
    else:
        return 0


def checkOdd(n):
    if n % 2 == 1:
        return 1
    else:
        return 0


def init(start, end, node, tree):
    if start == end:
        if tree[0] == 2:
            tree[node] = data_even[start]
        elif tree[0] == 1:
            tree[node] = data_odd[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node*2, tree) + init(mid+1, end, node*2+1, tree)
        return tree[node]
        

def prefixSum(start, end, node, left, right, tree):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return prefixSum(start, mid, node*2, left, right, tree) + prefixSum(mid+1, end, node*2+1, left, right, tree)


def update(start, end, node, index, diff, tree):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = diff
        return
    else:
        mid = (start + end) // 2
        update(start, mid, node*2, index, diff, tree)
        update(mid+1, end, node*2+1, index, diff, tree)
        tree[node] = tree[node*2] + tree[node*2+1]


n = int(input())
data = list(map(int, input().split()))
data_even = list(map(checkEven, data))
data_odd = list(map(checkOdd, data))
tree_even = [0] * (n*4)
tree_odd = [0] * (n*4)
tree_even[0] = 2
tree_odd[0] = 1
init(0, n-1, 1, tree_even)
init(0, n-1, 1, tree_odd)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        data_even[b-1] = checkEven(c)
        update(0, n-1, 1, b-1, checkEven(c), tree_even)
        data_odd[b-1] = checkOdd(c)
        update(0, n-1, 1, b-1, checkOdd(c), tree_odd)
    elif a == 2:
        print(prefixSum(0, n-1, 1, b-1, c-1, tree_even))
    elif a == 3:
        print(prefixSum(0, n-1, 1, b-1, c-1, tree_odd))
