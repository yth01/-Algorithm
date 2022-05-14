a = [[0 for i in range(19)] for j in range(19)]
for i in range(19):
    a[i] = list(map(int, input().split()))

n = int(input())
for i in range(n):
    row, column = map(int, input().split())
    for j in range(19):
        a[row-1][j] = int(a[row-1][j] == 0)
        a[j][column-1] = int(a[j][column-1] == 0)

for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print()