a = [[0 for i in range(19)] for j in range(19)]
n = int(input())
for i in range(n):
    row, column = map(int, input().split())
    a[row-1][column-1] = 1
for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print()