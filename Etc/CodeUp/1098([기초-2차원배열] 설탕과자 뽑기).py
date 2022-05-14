h, w = map(int, input().split())
a = [[0 for i in range(w)] for j in range(h)]

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    a[x - 1][y - 1] = 1
    for j in range(l):
        if d == 0:
            a[x - 1][y - 1 + j] = 1
        else:
            a[x - 1 + j][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()