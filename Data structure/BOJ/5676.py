import sys

def input():
    return sys.stdin.readline()[:-1]


def modify(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def init(start, end, node):
    if start == end:
        tree[node] = data[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, node*2) * init(mid+1, end, node*2+1)
        return tree[node]
        

def prefixMul(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return prefixMul(start, mid, node*2, left, right) * prefixMul(mid+1, end, node*2+1, left, right)


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
        tree[node] = tree[node*2] * tree[node*2+1]


while True:
    try:
        n, k = map(int, input().split())
        data = list(map(int, input().split()))
        data = list(map(modify, data))
        tree = [0] * (n*4)
        init(0, n-1, 1)
        for _ in range(k):
            cmd = input().split()
            a, b = map(int, [cmd[1], cmd[2]])
            if cmd[0] == 'C':
                data[a-1] = b
                update(0, n-1, 1, a-1, modify(b))
            elif cmd[0] == 'P':
                result = prefixMul(0, n-1, 1, a-1, b-1)
                if result > 0:
                    print("+", end='')
                elif result < 0:
                    print("-", end='')
                else:
                    print("0", end='')
        print()
    except:
        break
