a = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    a[i] = list(map(int, input().split()))

x = 1
y = 1
check = 0
check = 1 if a[x][y] == 2 else 0
a[x][y] = 9

while a[x+1][y] * a[x][y+1] != 1:
    if check == 1:
        break
    if a[x][y+1] == 2:
        y += 1
        a[x][y] = 9
        break
    if a[x][y+1] != 1:
        y += 1
        a[x][y] = 9
        continue
    if a[x+1][y] == 2:
        x += 1
        a[x][y] = 9
        break
    if a[x][y+1] == 1:
        x += 1
        a[x][y] = 9
        continue

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()
